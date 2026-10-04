#!/usr/bin/env python3
"""Consolidar JSON normalizado; preservar moedas e precisão decimal."""
import argparse
import csv
import json
import re
from datetime import date
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path


def safe_cell(text):
    return "'"+text if text.lstrip().startswith(('=', '+', '-', '@')) else text


def consolidate(records):
    if not isinstance(records, list):
        raise ValueError('A entrada deve ser uma lista JSON')
    validated, ids = [], set()
    for n, row in enumerate(records, 1):
        if not isinstance(row, dict):
            raise ValueError(f'Linha {n}: esperado objeto')
        for key in ('date', 'amount', 'currency', 'category', 'source'):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise ValueError(f'Linha {n}: {key} precisa ser string preenchida')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', row['date']):
            raise ValueError(f'Linha {n}: data deve ser YYYY-MM-DD')
        date.fromisoformat(row['date'])
        if not re.fullmatch(r'[A-Z]{3}', row['currency']):
            raise ValueError(f'Linha {n}: moeda deve ter três letras maiúsculas')
        if not re.fullmatch(r'-?\d+(?:\.\d+)?', row['amount']):
            raise ValueError(f'Linha {n}: valor decimal inválido')
        try:
            amount = Decimal(row['amount'])
        except InvalidOperation as exc:
            raise ValueError(f'Linha {n}: valor decimal inválido') from exc
        identifier = row.get('id')
        if identifier is not None:
            if not isinstance(identifier, str) or not identifier.strip() or identifier in ids:
                raise ValueError(f'Linha {n}: ID inválido ou repetido')
            ids.add(identifier)
        validated.append((row, amount))
    groups = {}
    # Precisão dimensionada para somas exatas, incluindo estornos.
    with localcontext() as ctx:
        ctx.prec = max([28]+[len(r['amount']) for r, a in validated]) + len(str(len(validated))) + 2
        for row, amount in validated:
            key = (row['date'][:7], row['currency'], row['category'])
            count, total = groups.get(key, (0, Decimal(0)))
            groups[key] = (count+1, total+amount)
    return [{'month':k[0], 'currency':k[1], 'category':safe_cell(k[2]), 'count':v[0], 'amount':format(v[1], 'f')} for k,v in sorted(groups.items())]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input', type=Path)
    p.add_argument('output', type=Path)
    a = p.parse_args()
    try:
        if a.output.exists() or a.input.resolve() == a.output.resolve():
            raise ValueError('A saída já existe ou coincide com a entrada')
        rows = consolidate(json.loads(a.input.read_text(encoding='utf-8')))
        with a.output.open('x', encoding='utf-8', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=['month','currency','category','count','amount'])
            writer.writeheader()
            writer.writerows(rows)
    except (OSError, ValueError) as exc:
        p.exit(1, str(exc)+'\n')

if __name__ == '__main__':
    main()
