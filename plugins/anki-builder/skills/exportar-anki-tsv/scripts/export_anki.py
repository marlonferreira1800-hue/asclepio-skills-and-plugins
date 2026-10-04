#!/usr/bin/env python3
"""Exportar JSON de cartões Basic/Cloze para TSV UTF-8 sem cabeçalho."""
import argparse
import csv
import html
import json
import pathlib
import re


def field(value):
    if not isinstance(value, str):
        raise ValueError('Campos de cartões devem ser strings.')
    return html.escape(value, quote=False).replace('\r\n', '\n').replace('\r', '\n').replace('\n', '<br>').replace('\t', '    ')


def export(cards, model):
    if not isinstance(cards, list) or not cards:
        raise ValueError('Forneça uma lista não vazia de cartões.')
    fields = ('front', 'back') if model == 'basic' else ('text', 'extra')
    rows = []
    seen = set()
    for number, card in enumerate(cards, 1):
        if not isinstance(card, dict):
            raise ValueError(f'Cartão {number}: objeto esperado.')
        if fields[0] not in card or (model == 'basic' and fields[1] not in card):
            raise ValueError(f'Cartão {number}: faltam campos {fields}.')
        first = card[fields[0]]
        second = card.get(fields[1], '')
        if not isinstance(first, str) or not first.strip():
            raise ValueError(f'Cartão {number}: frente/texto vazio.')
        if model == 'basic' and (not isinstance(second, str) or not second.strip()):
            raise ValueError(f'Cartão {number}: verso vazio.')
        if model == 'cloze' and not re.search(r'\{\{c[1-9]\d*::.+?\}\}', first, re.DOTALL):
            raise ValueError(f'Cartão {number}: lacuna cloze válida não encontrada.')
        if model == 'cloze' and (first.count('{{') != first.count('}}')):
            raise ValueError(f'Cartão {number}: chaves cloze não balanceadas.')
        if first.strip() in seen:
            raise ValueError(f'Cartão {number}: frente/texto duplicado.')
        seen.add(first.strip())
        tags = card.get('tags', [])
        if not isinstance(tags, list) or not all(isinstance(tag, str) and tag and not any(ch.isspace() for ch in tag) and not any(ch in '<>&' for ch in tag) for tag in tags):
            raise ValueError(f'Cartão {number}: tags devem ser lista de palavras sem espaços/HTML.')
        if card.get('source'):
            if not isinstance(card['source'], str) or not isinstance(second, str):
                raise ValueError(f'Cartão {number}: fonte e conteúdo devem ser strings.')
            second += '\nFonte: ' + card['source']
        rows.append((field(first), field(second), ' '.join(tags)))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=pathlib.Path)
    parser.add_argument('output', type=pathlib.Path)
    parser.add_argument('--model', choices=['basic', 'cloze'], default='basic')
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.error('Entrada e saída precisam ser diferentes.')
    if args.output.exists():
        parser.error('A saída já existe; escolha um caminho novo.')
    try:
        rows = export(json.loads(args.input.read_text(encoding='utf-8')), args.model)
        with args.output.open('x', encoding='utf-8', newline='') as stream:
            csv.writer(stream, delimiter='\t', lineterminator='\n').writerows(rows)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Erro: {exc}\n')
    print(json.dumps({'cards': len(rows), 'model': args.model, 'output': str(args.output)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
