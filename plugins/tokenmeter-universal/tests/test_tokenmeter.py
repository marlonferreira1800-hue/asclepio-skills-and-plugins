import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/medir-tokens/scripts/tokenmeter.py'
spec = importlib.util.spec_from_file_location('tokenmeter', SCRIPT)
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)

def event(i='a', **kwargs):
    return dict(id=i, timestamp='2026-09-30T16:00:00-03:00', provider='test', input_tokens=100, output_tokens=20, **kwargs)

class Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = str(Path(self.tmp.name)/'usage.sqlite3')
        self.ledger = t.Ledger(self.db)
    def tearDown(self):
        self.ledger.db.close()
        self.tmp.cleanup()
    def test_openai_cache_reasoning_not_double_counted(self):
        e,_ = t.normalize({'response':{'id':'r','created':1790794800,'usage':{'input_tokens':1000,'output_tokens':100,'total_tokens':1100,'input_tokens_details':{'cached_tokens':500},'output_tokens_details':{'reasoning_tokens':80}}}})
        self.assertEqual(e['total_tokens'],1100)
        self.assertEqual(e['reasoning_tokens'],80)
    def test_anthropic_cache_adds_to_input(self):
        e,_ = t.normalize({'provider':'anthropic','usage':{'input_tokens':10,'output_tokens':3,'cache_creation_input_tokens':40,'cache_read_input_tokens':100}})
        self.assertEqual(e['input_tokens'],150)
        self.assertEqual(e['total_tokens'],153)
    def test_gemini_preserves_authoritative_total(self):
        e,_=t.normalize({'usageMetadata':{'promptTokenCount':100,'candidatesTokenCount':20,'thoughtsTokenCount':5,'totalTokenCount':130}})
        self.assertEqual(e['output_tokens'],25)
        self.assertEqual(e['other_tokens'],5)
        self.assertEqual(e['total_tokens'],130)
    def test_compatible_and_ollama(self):
        a,_=t.normalize({'usage':{'prompt_tokens':9,'completion_tokens':1}})
        b,_=t.normalize({'prompt_eval_count':40,'eval_count':10})
        self.assertEqual((a['total_tokens'],b['total_tokens']),(10,50))
    def test_atomic_import_and_duplicate_conflict(self):
        self.ledger.add_many([event()])
        self.assertEqual(self.ledger.add_many([event()])['skipped'],1)
        changed=event(); changed['input_tokens']=101
        with self.assertRaises(ValueError): self.ledger.add_many([event('b'),changed])
        self.assertEqual(len(self.ledger.events()),1)
    def test_duplicate_without_timestamp(self):
        e=event(); del e['timestamp']
        self.ledger.add_many([e])
        self.assertEqual(self.ledger.add_many([e])['skipped'],1)
    def test_separate_accounts(self):
        self.ledger.add_many([event(account='a'),event(account='b')])
        self.assertEqual(self.ledger.report('all')['records'],2)
    def test_local_day_boundaries(self):
        a,b=event('a'),event('b')
        a['timestamp']='2026-10-01T02:59:59Z'; b['timestamp']='2026-10-01T03:00:00Z'
        self.ledger.add_many([a,b])
        self.assertEqual(self.ledger.report('day','2026-09-30')['records'],1)
        self.assertEqual(self.ledger.report('month','2026-10-01')['records'],1)
    def test_calendar_week_month_year(self):
        self.assertEqual(t.bounds('week',date(2026,1,1)),(date(2025,12,29),date(2026,1,5)))
        self.assertEqual(t.bounds('month',date(2026,12,31)),(date(2026,12,1),date(2027,1,1)))
        self.assertEqual(t.bounds('month',date(2024,2,29)),(date(2024,2,1),date(2024,3,1)))
    def test_invalid_counts_dates_subsets_and_prices(self):
        for field,value in [('input_tokens',-1),('output_tokens',1.5),('input_tokens',True),('timestamp','2026-09-30'),('cached_input_tokens',101),('reasoning_tokens',21),('total_tokens',999),('cost_amount','NaN')]:
            e=event(); e[field]=value
            with self.assertRaises((ValueError,KeyError)): t.normalize(e)
        with self.assertRaises(KeyError): t.normalize({'usage':{'input_tokens':3}})
    def test_costs_unknown_and_currencies(self):
        self.ledger.add_many([event('a',cost_amount='1.25',currency='USD'),event('b',cost_amount='3',currency='BRL'),event('c')])
        r=self.ledger.report('all')
        self.assertEqual(r['costs'],{'USD':'1.25','BRL':'3'})
        self.assertEqual(r['records_without_cost'],1)
    def test_rate_subsets_and_missing_rate(self):
        e,_=t.normalize(event(cached_input_tokens=50,rates={'currency':'USD','as_of':'2026-09-30','input_per_million':2,'cached_per_million':1,'output_per_million':4}))
        self.assertEqual(t.cost(e),('USD',Decimal('0.00023')))
        del e['rates']['cached_per_million']; self.assertIsNone(t.cost(e))
    def test_backup_roundtrip_and_csv_formula_escape(self):
        self.ledger.add_many([event(model='=HYPERLINK("bad")')])
        p=Path(self.tmp.name)/'backup.json'; t.export(self.ledger,'json',p)
        other=t.Ledger(Path(self.tmp.name)/'other.sqlite3')
        self.assertEqual(other.add_many(t.read_records(p))['added'],1)
        other.db.close()
        p=Path(self.tmp.name)/'usage.csv';t.export(self.ledger,'csv',p)
        self.assertEqual(t.read_records(p)[0]['model'][0],"'")
    def test_budget_and_empty_coverage(self):
        r=self.ledger.report('all');self.assertIsNone(r['coverage']['first_record'])
        self.ledger.add_many([event()])
        self.assertTrue(self.ledger.report('all',budget_tokens=100)['budget']['exceeded'])
    def test_html_escape(self):
        self.ledger.add_many([event(model='<script>alert(1)</script>')])
        p=Path(self.tmp.name)/'dashboard.html'; t.dashboard(self.ledger,p,'America/Sao_Paulo','2026-09-30')
        self.assertNotIn('<script>alert(1)</script>',p.read_text())
        self.assertIn('&lt;script&gt;',p.read_text())
    def test_mcp_subprocess_protocol_and_tools(self):
        requests=[{'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-03-26'}}, {'jsonrpc':'2.0','method':'notifications/initialized'}, {'jsonrpc':'2.0','id':2,'method':'tools/list'}, {'jsonrpc':'2.0','id':3,'method':'tools/call','params':{'name':'record_usage','arguments':{'record':event()}}}, {'jsonrpc':'2.0','id':4,'method':'tools/call','params':{'name':'report_usage','arguments':{'period':'all'}}}]
        p=subprocess.run([sys.executable,str(SCRIPT),'--db',self.db,'mcp'],input=''.join(json.dumps(r)+'\n' for r in requests),text=True,capture_output=True,check=True)
        out=[json.loads(s) for s in p.stdout.splitlines()]
        self.assertEqual(len(out),4)
        self.assertEqual(len(out[1]['result']['tools']),3)
        self.assertEqual(json.loads(out[3]['result']['content'][0]['text'])['totals']['total_tokens'],120)
    def test_estimate_marks_approximation(self):
        self.assertEqual(t.estimate('abcde')['estimated_tokens'],2)
        self.assertEqual(t.estimate('abcde')['quality'],'estimated')

if __name__=='__main__': unittest.main()
