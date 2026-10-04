#!/usr/bin/env python3
"""Simulação de compra à vista; entrada e stop são premissas do usuário."""
import argparse
import json
from decimal import Decimal, InvalidOperation, ROUND_FLOOR

def positive(value):
    try:
        number = Decimal(value)
    except InvalidOperation:
        raise argparse.ArgumentTypeError('Informe um número válido.')
    if not number.is_finite() or number <= 0:
        raise argparse.ArgumentTypeError('Informe um número finito maior que zero.')
    return number

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ('capital', 'risk-pct', 'entry', 'stop', 'max-allocation-pct'):
        parser.add_argument('--' + field, type=positive, required=True)
    parser.add_argument('--lot', type=int, default=1)
    args = parser.parse_args()
    if args.risk_pct > 100 or args.max_allocation_pct > 100 or args.lot < 1:
        parser.error('Percentuais devem ser <= 100 e lote deve ser >= 1.')
    if args.stop >= args.entry:
        parser.error('Para compra à vista, stop deve ser inferior à entrada.')
    budget = args.capital * args.risk_pct / 100
    cap = args.capital * args.max_allocation_pct / 100
    distance = args.entry - args.stop
    lots = (min(budget / distance, cap / args.entry) / args.lot).to_integral_value(rounding=ROUND_FLOOR)
    units = int(lots) * args.lot
    print(json.dumps({'units': units, 'risk_budget': str(budget), 'allocated': str(units * args.entry), 'nominal_loss_at_stop': str(units * distance), 'scope': 'Compra à vista; exclui taxas, slippage e gaps; stop não garante execução.'}, ensure_ascii=False))

if __name__ == '__main__':
    main()
