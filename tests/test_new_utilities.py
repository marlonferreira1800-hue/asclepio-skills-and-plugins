import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
def load(relative):
    path = ROOT/relative
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

INV = load('plugins/arquivo-inteligente/skills/classificar-arquivos/scripts/inventory.py')
EXP = load('plugins/recibos-despesas/skills/consolidar-despesas/scripts/consolidate.py')

class Utilities(unittest.TestCase):
    def test_inventory_hash_and_exclusions(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'a.txt').write_text('ação')
            (root/'b.txt').write_text('ação')
            (root/'empty.txt').write_text('')
            (root/'.env').write_text('secret')
            (root/'link').symlink_to(root/'a.txt')
            (root/'node_modules').mkdir()
            (root/'node_modules'/'skip').write_text('x')
            result = INV.inventory(root, True)
            self.assertEqual(result['duplicates'], [['a.txt','b.txt']])
            self.assertEqual(len(result['files']),3)
            self.assertEqual(result['errors'],[])
            self.assertEqual((root/'a.txt').read_text(),'ação')
            self.assertEqual(INV.inventory(root)['duplicates'],[])

    def test_exact_amount_currency_and_refunds(self):
        records = [dict(date='2026-01-03', amount=a, currency=c, category='Curso', source='recibo') for a,c in [('0.10','BRL'),('0.20','BRL'),('-0.05','BRL'),('10','USD')]]
        result = EXP.consolidate(records)
        self.assertEqual(result[0]['amount'],'0.25')
        self.assertEqual(result[0]['count'],3)
        self.assertEqual(result[1]['amount'],'10')

    def test_invalid_records_and_ids(self):
        base = dict(date='2026-01-03', amount='1.00', currency='BRL', category='Curso', source='recibo')
        for change in [dict(date='2026-02-30'),dict(amount='NaN'),dict(amount=0.1),dict(source=''),dict(currency='')]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                EXP.consolidate([base|change])
        with self.assertRaises(ValueError):
            EXP.consolidate([base|{'id':'A'},base|{'id':'A'}])

    def test_csv_formula_category(self):
        row = dict(date='2026-01-03', amount='1', currency='BRL', category='  =HYPERLINK("x")', source='recibo')
        self.assertTrue(EXP.consolidate([row])[0]['category'].startswith("'"))

    def test_cli_no_overwrite_and_invalid_no_output(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            src, out = root/'in.json', root/'out.csv'
            src.write_text(json.dumps([{'amount': 'NaN'}]))
            cmd = [sys.executable, EXP.__file__, str(src), str(out)]
            self.assertNotEqual(subprocess.run(cmd,capture_output=True).returncode,0)
            self.assertFalse(out.exists())
            out.write_text('preservado')
            self.assertNotEqual(subprocess.run(cmd,capture_output=True).returncode,0)
            self.assertEqual(out.read_text(),'preservado')
            cmd = [sys.executable, INV.__file__, '--root', str(root), '--output', str(out)]
            self.assertNotEqual(subprocess.run(cmd,capture_output=True).returncode,0)
            self.assertEqual(out.read_text(),'preservado')

if __name__ == '__main__':
    unittest.main()
