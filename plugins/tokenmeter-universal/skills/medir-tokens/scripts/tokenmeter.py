#!/usr/bin/env python3
"""Offline usage ledger, reports, exports, HTML dashboard and MCP stdio. Python 3.10+."""
import argparse
import csv
import hashlib
import html
import json
import math
import os
import sqlite3
import sys
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from zoneinfo import ZoneInfo

VERSION = '1.0.0'
COUNTS = ('input_tokens', 'output_tokens', 'cached_input_tokens', 'cache_write_tokens',
          'reasoning_tokens', 'other_tokens', 'total_tokens')
QUALITIES = ('reported', 'manual', 'estimated', 'local_tokenizer')


def count(value):
    if isinstance(value, bool): raise ValueError('Token count cannot be boolean')
    try: number = Decimal(str(value))
    except InvalidOperation as exc: raise ValueError('Invalid token count') from exc
    if not number.is_finite() or number < 0 or number != number.to_integral_value():
        raise ValueError('Token counts must be nonnegative integers')
    return int(number)


def instant(value=None):
    if value is None: return datetime.now(timezone.utc)
    if isinstance(value, (int, float)): return datetime.fromtimestamp(value, timezone.utc)
    dt = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    if dt.tzinfo is None: raise ValueError('Timestamp needs an explicit UTC offset')
    return dt.astimezone(timezone.utc)


def decimal_amount(value):
    try: d = Decimal(str(value))
    except InvalidOperation as exc: raise ValueError('Invalid monetary value') from exc
    if not d.is_finite() or d < 0: raise ValueError('Monetary value must be finite and nonnegative')
    return d


def cost(e):
    if 'cost_amount' in e:
        if not e.get('currency'): raise ValueError('cost_amount requires currency')
        return str(e['currency']), decimal_amount(e['cost_amount'])
    rates = e.get('rates')
    if not rates: return None
    if not isinstance(rates, dict) or not rates.get('currency') or not rates.get('as_of'):
        raise ValueError('rates requires currency and as_of')
    date.fromisoformat(rates['as_of'])
    for key in ('input_per_million', 'cached_per_million', 'cache_write_per_million', 'output_per_million'):
        if key in rates: decimal_amount(rates[key])
    categories = [(e['input_tokens'] - e['cached_input_tokens'] - e['cache_write_tokens'], 'input_per_million'),
                  (e['cached_input_tokens'], 'cached_per_million'), (e['cache_write_tokens'], 'cache_write_per_million'),
                  (e['output_tokens'], 'output_per_million')]
    if e['other_tokens'] or any(n and key not in rates for n, key in categories): return None
    return str(rates['currency']), sum((Decimal(n) * decimal_amount(rates.get(key, 0)) for n, key in categories), Decimal(0)) / 1000000


def normalize(data):
    if not isinstance(data, dict): raise ValueError('Each record must be an object')
    response = data.get('response', data)
    if not isinstance(response, dict): raise ValueError('response must be an object')
    provider = str(data.get('provider', '')).lower()
    usage, meta = response.get('usage'), response.get('usageMetadata')
    warnings = []
    c = dict.fromkeys(COUNTS, 0)
    if meta is not None:
        provider = provider or 'gemini'
        c['input_tokens'] = count(meta['promptTokenCount'])
        c['reasoning_tokens'] = count(meta.get('thoughtsTokenCount', 0))
        c['output_tokens'] = count(meta['candidatesTokenCount']) + c['reasoning_tokens']
        c['cached_input_tokens'] = count(meta.get('cachedContentTokenCount', 0))
        total = count(meta.get('totalTokenCount', c['input_tokens'] + c['output_tokens']))
        c['other_tokens'] = total - c['input_tokens'] - c['output_tokens']
    elif usage is not None:
        if provider in ('anthropic', 'claude') or any(k in usage for k in ('cache_read_input_tokens', 'cache_creation_input_tokens')):
            provider = provider or 'anthropic'
            c['cached_input_tokens'] = count(usage.get('cache_read_input_tokens', 0))
            c['cache_write_tokens'] = count(usage.get('cache_creation_input_tokens', 0))
            c['input_tokens'] = count(usage['input_tokens']) + c['cached_input_tokens'] + c['cache_write_tokens']
            c['output_tokens'] = count(usage['output_tokens'])
        else:
            provider = provider or 'openai-compatible'
            c['input_tokens'] = count(usage['input_tokens'] if 'input_tokens' in usage else usage['prompt_tokens'])
            c['output_tokens'] = count(usage['output_tokens'] if 'output_tokens' in usage else usage['completion_tokens'])
            detail = usage.get('input_tokens_details') or usage.get('prompt_tokens_details') or {}
            c['cached_input_tokens'] = count(detail.get('cached_tokens', 0))
            c['cache_write_tokens'] = count(detail.get('cache_write_tokens', 0))
            detail = usage.get('output_tokens_details') or usage.get('completion_tokens_details') or {}
            c['reasoning_tokens'] = count(detail.get('reasoning_tokens', 0))
            if 'total_tokens' in usage and count(usage['total_tokens']) != c['input_tokens'] + c['output_tokens']:
                raise ValueError('API total_tokens does not match input + output')
    elif 'prompt_eval_count' in response:
        provider = provider or 'ollama'
        c['input_tokens'] = count(response['prompt_eval_count'])
        c['output_tokens'] = count(response['eval_count'])
    else:
        provider = provider or 'custom'
        if 'input_tokens' not in data or 'output_tokens' not in data:
            raise ValueError('Both input_tokens and output_tokens are required')
        for field in COUNTS[:-1]: c[field] = count(data.get(field, 0))
    if c['other_tokens'] < 0: raise ValueError('Reported total is smaller than known components')
    c['total_tokens'] = c['input_tokens'] + c['output_tokens'] + c['other_tokens']
    if usage is None and meta is None and 'total_tokens' in data and count(data['total_tokens']) != c['total_tokens']:
        raise ValueError('Canonical total_tokens does not match components')
    if c['cached_input_tokens'] + c['cache_write_tokens'] > c['input_tokens'] or c['reasoning_tokens'] > c['output_tokens']:
        raise ValueError('Cache/reasoning subsets exceed parent counts')
    quality = data.get('quality', 'reported' if usage is not None or meta is not None or 'prompt_eval_count' in response else 'manual')
    if quality not in QUALITIES: raise ValueError('Invalid quality category')
    timestamp = data.get('timestamp', response.get('created_at', response.get('created')))
    if timestamp is None: warnings.append('Missing timestamp: recorded at import time; supply timestamp for historical data')
    event = dict(provider=provider, platform=str(data.get('platform', provider)), account=str(data.get('account', 'default')),
                 model=str(data.get('model', response.get('model', response.get('modelVersion', 'unknown')))),
                 timestamp=instant(timestamp).isoformat(), quality=quality,
                 source=str(data.get('source', 'api-usage' if quality == 'reported' else quality)), **c)
    for optional in ('cost_amount', 'currency', 'rates'):
        if optional in data and data[optional] not in ('', None): event[optional] = data[optional]
    cost(event)
    event_id = data.get('id', response.get('id', response.get('responseId')))
    if event_id is None:
        event_id = hashlib.sha256(json.dumps(event, sort_keys=True).encode()).hexdigest()
        warnings.append('No request ID: deduplication uses full normalized record only')
    event['id'] = str(event_id)
    return event, warnings


def bounds(period, day):
    if period == 'all': return None, None
    if period == 'day': return day, day + timedelta(days=1)
    if period == 'week':
        start = day - timedelta(days=day.weekday())
        return start, start + timedelta(days=7)
    if period == 'month':
        return day.replace(day=1), date(day.year + (day.month == 12), 1 if day.month == 12 else day.month + 1, 1)
    if period == 'year': return date(day.year, 1, 1), date(day.year + 1, 1, 1)
    raise ValueError('period must be day/week/month/year/all')


class Ledger:
    def __init__(self, path=None):
        p = Path(path or os.environ.get('TOKENMETER_DB', str(Path.home() / '.tokenmeter' / 'usage.sqlite3'))).expanduser()
        p.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(p), timeout=30)
        self.db.execute('CREATE TABLE IF NOT EXISTS events (key TEXT PRIMARY KEY, body TEXT NOT NULL)')

    def add_many(self, records):
        normalized = [normalize(r) for r in records]
        added = skipped = 0
        warnings = []
        with self.db:
            for e, w in normalized:
                key = json.dumps([e[k] for k in ('provider', 'platform', 'account', 'id')])
                body = json.dumps(e, sort_keys=True, ensure_ascii=False)
                old = self.db.execute('SELECT body FROM events WHERE key=?', (key,)).fetchone()
                if old:
                    if any(msg.startswith('Missing timestamp:') for msg in w):
                        e['timestamp'] = json.loads(old[0])['timestamp']
                        body = json.dumps(e, sort_keys=True, ensure_ascii=False)
                    if old[0] != body: raise ValueError('Duplicate ID has conflicting data: ' + e['id'])
                    skipped += 1
                else:
                    self.db.execute('INSERT INTO events VALUES (?,?)', (key, body))
                    added += 1
                warnings.extend(w)
        return dict(added=added, skipped=skipped, warnings=sorted(set(warnings)))

    def events(self):
        return [json.loads(r[0]) for r in self.db.execute('SELECT body FROM events ORDER BY key')]

    def report(self, period='month', at=None, tz='America/Sao_Paulo', provider=None, platform=None, model=None, account=None, budget_tokens=None):
        zone = ZoneInfo(tz)
        anchor = date.fromisoformat(at) if at else datetime.now(zone).date()
        start, end = bounds(period, anchor)
        events = []
        for e in self.events():
            day = instant(e['timestamp']).astimezone(zone).date()
            if start and not start <= day < end: continue
            if any(v is not None and e[k] != v for k, v in (('provider', provider), ('platform', platform), ('model', model), ('account', account))): continue
            events.append(e)
        totals = {k:sum(e[k] for e in events) for k in COUNTS}
        groups, qualities, monetary = {}, {}, {}
        unknown = 0
        for e in events:
            k = json.dumps([e['provider'], e['platform'], e['model'], e['account']], ensure_ascii=False)
            groups[k] = groups.get(k, 0) + e['total_tokens']
            q = qualities.setdefault(e['quality'], dict(records=0, total_tokens=0))
            q['records'] += 1; q['total_tokens'] += e['total_tokens']
            amount = cost(e)
            if amount:
                currency, n = amount
                monetary[currency] = monetary.get(currency, Decimal(0)) + n
            else: unknown += 1
        stamps = sorted(e['timestamp'] for e in events)
        result = dict(period=period, timezone=tz, start=str(start) if start else None, end_exclusive=str(end) if end else None,
                      records=len(events), totals=totals, by_provider_platform_model_account=groups, by_quality=qualities,
                      costs={k:str(v) for k,v in monetary.items()}, records_without_cost=unknown,
                      coverage=dict(first_record=stamps[0] if stamps else None, last_record=stamps[-1] if stamps else None),
                      notice='Only recorded usage; empty ledger means no data, not proof of zero account consumption.')
        if budget_tokens is not None:
            budget = count(budget_tokens)
            result['budget'] = dict(limit_tokens=budget, exceeded=totals['total_tokens'] > budget,
                                    remaining_tokens=max(0, budget - totals['total_tokens']))
        return result


def read_records(path):
    p = Path(path)
    if p.suffix.lower() == '.csv':
        with p.open(encoding='utf-8-sig', newline='') as f: records = list(csv.DictReader(f))
        for r in records:
            if r.get('rates'): r['rates'] = json.loads(r['rates'])
        return records
    text = p.read_text(encoding='utf-8-sig')
    if p.suffix.lower() == '.jsonl': return [json.loads(line) for line in text.splitlines() if line.strip()]
    data = json.loads(text)
    return data if isinstance(data, list) else [data]


def estimate(text):
    if not isinstance(text, str): raise ValueError('text must be a string')
    return dict(estimated_tokens=math.ceil(len(text) / 4), quality='estimated', method='ceil(unicode_characters / 4)',
                notice='Rough text-only estimate; not provider billing, multimodal, hidden context or reasoning usage.')


def export(ledger, fmt, path):
    events, p = ledger.events(), Path(path)
    if fmt == 'json': p.write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding='utf-8')
    else:
        columns = ['id', 'timestamp', 'provider', 'platform', 'account', 'model', 'quality', 'source', *COUNTS, 'cost_amount', 'currency', 'rates']
        with p.open('w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=columns); writer.writeheader()
            for e in events:
                row = {k:e.get(k, '') for k in columns}
                if row['rates']: row['rates'] = json.dumps(row['rates'], ensure_ascii=False)
                for k, value in row.items():
                    if isinstance(value, str) and value.startswith(('=', '+', '-', '@', '\t', '\r')): row[k] = "'" + value
                writer.writerow(row)
    return dict(path=str(p.resolve()), records=len(events))


def dashboard(ledger, path, tz, at):
    reports = [ledger.report(p, at, tz) for p in ('day', 'week', 'month', 'year', 'all')]
    labels = ['Dia escolhido', 'Semana', 'Mês', 'Ano', 'Total acumulado']
    cards = ''.join('<article><h2>' + label + '</h2><strong>' + format(r['totals']['total_tokens'], ',') +
                    '</strong><p>' + str(r['records']) + ' registros</p><p>Entrada: ' + str(r['totals']['input_tokens']) +
                    ' · Saída: ' + str(r['totals']['output_tokens']) + '</p></article>' for label,r in zip(labels,reports))
    summary = reports[-1]
    rows = ''.join('<tr><td>' + html.escape(q) + '</td><td>' + str(v['records']) + '</td><td>' + str(v['total_tokens']) + '</td></tr>' for q,v in summary['by_quality'].items())
    blob = '<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TokenMeter Universal</title><style>body{font:16px system-ui;background:#f3f6fc;color:#16243e;margin:32px auto;max-width:1100px;padding:20px}section{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px}article{background:white;padding:20px;border-radius:16px;border:1px solid #dfe7f6}h2{font-size:17px}strong{font-size:30px;color:#2858b8}table{width:100%;background:white;border-collapse:collapse}th,td{text-align:left;padding:12px;border-bottom:1px solid #eee}pre{white-space:pre-wrap;overflow-wrap:anywhere}small{color:#53637a}</style><h1>TokenMeter Universal</h1><p>Consumo registrado · ' + html.escape(tz) + '</p><section>' + cards + '</section><h2>Qualidade dos dados · total acumulado</h2><table><tr><th>Categoria</th><th>Registros</th><th>Tokens</th></tr>' + rows + '</table><p>Custos conhecidos: ' + html.escape(json.dumps(summary['costs'])) + ' · Sem preço: ' + str(summary['records_without_cost']) + '</p><small>Painel estático dos registros locais. Ausência de dados não comprova consumo zero. Atualize executando dashboard novamente. Cache e raciocínio já estão incluídos nos totais.</small><details><summary>Relatórios completos</summary><pre>' + html.escape(json.dumps(reports, ensure_ascii=False, indent=2)) + '</pre></details></html>'
    Path(path).write_text(blob, encoding='utf-8')
    return dict(path=str(Path(path).resolve()))


def mcp(ledger):
    tools = [
        dict(name='record_usage', description='Record final API usage or canonical metadata; not automatic monitoring.', inputSchema={'type':'object','properties':{'record':{'type':'object'}},'required':['record'],'additionalProperties':False}),
        dict(name='report_usage', description='Report recorded tokens by calendar period, quality and currency.', inputSchema={'type':'object','properties':{'period':{'type':'string','enum':['day','week','month','year','all']},'at':{'type':'string'},'tz':{'type':'string'},'provider':{'type':'string'},'platform':{'type':'string'},'account':{'type':'string'},'model':{'type':'string'},'budget_tokens':{'type':'integer','minimum':0}},'additionalProperties':False}),
        dict(name='estimate_text', description='Characters/4 text estimate; never billed usage.', inputSchema={'type':'object','properties':{'text':{'type':'string'}},'required':['text'],'additionalProperties':False})]
    for line in sys.stdin:
        req = None
        try:
            req = json.loads(line)
            if not isinstance(req, dict) or req.get('jsonrpc') != '2.0' or not isinstance(req.get('method'), str): raise ValueError('Invalid JSON-RPC request')
            if 'id' not in req: continue
            method, params = req['method'], req.get('params', {})
            if method == 'initialize':
                version = params.get('protocolVersion')
                version = version if version in ('2024-11-05', '2025-03-26', '2025-06-18') else '2025-03-26'
                result = dict(protocolVersion=version, capabilities={'tools':{}}, serverInfo={'name':'tokenmeter-universal','version':VERSION})
            elif method == 'ping': result = {}
            elif method == 'tools/list': result = {'tools':tools}
            elif method == 'tools/call':
                name, args = params.get('name'), params.get('arguments', {})
                try:
                    if name == 'record_usage': payload = ledger.add_many([args['record']])
                    elif name == 'report_usage': payload = ledger.report(**args)
                    elif name == 'estimate_text': payload = estimate(args['text'])
                    else: raise ValueError('Unknown tool: ' + str(name))
                    result = {'content':[{'type':'text','text':json.dumps(payload, ensure_ascii=False)}]}
                except Exception as exc:
                    result = {'isError':True,'content':[{'type':'text','text':str(exc)}]}
            else:
                print(json.dumps({'jsonrpc':'2.0','id':req['id'],'error':{'code':-32601,'message':'Method not found'}}), flush=True)
                continue
            out = {'jsonrpc':'2.0','id':req['id'],'result':result}
        except json.JSONDecodeError: out = {'jsonrpc':'2.0','id':None,'error':{'code':-32700,'message':'Parse error'}}
        except Exception as exc:
            out = {'jsonrpc':'2.0','id':req.get('id') if isinstance(req, dict) else None,'error':{'code':-32602,'message':str(exc)}}
        print(json.dumps(out, ensure_ascii=False), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', help='SQLite path; default TOKENMETER_DB or ~/.tokenmeter/usage.sqlite3')
    sub = parser.add_subparsers(dest='command', required=True)
    imp = sub.add_parser('import'); imp.add_argument('file')
    rec = sub.add_parser('record'); rec.add_argument('json_record')
    rep = sub.add_parser('report')
    rep.add_argument('--period', choices=['day','week','month','year','all'], default='month')
    rep.add_argument('--at'); rep.add_argument('--tz', default='America/Sao_Paulo')
    for field in ('provider', 'platform', 'account', 'model'): rep.add_argument('--' + field)
    rep.add_argument('--budget-tokens', type=int)
    ex = sub.add_parser('export'); ex.add_argument('--format', choices=['csv','json'], default='json'); ex.add_argument('--out', required=True)
    dash = sub.add_parser('dashboard'); dash.add_argument('--out', default='painel.html'); dash.add_argument('--tz', default='America/Sao_Paulo'); dash.add_argument('--at')
    est = sub.add_parser('estimate'); est.add_argument('--text', required=True)
    sub.add_parser('mcp')
    args = parser.parse_args()
    try:
        if args.command == 'estimate': result = estimate(args.text)
        else:
            ledger = Ledger(args.db)
            if args.command == 'mcp': mcp(ledger); return
            if args.command == 'import': result = ledger.add_many(read_records(args.file))
            elif args.command == 'record': result = ledger.add_many([json.loads(args.json_record)])
            elif args.command == 'report': result = ledger.report(**{k:v for k,v in vars(args).items() if k not in ('db','command')})
            elif args.command == 'export': result = export(ledger, args.format, args.out)
            elif args.command == 'dashboard': result = dashboard(ledger, args.out, args.tz, args.at)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as exc:
        print('TokenMeter: ' + str(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__': main()
