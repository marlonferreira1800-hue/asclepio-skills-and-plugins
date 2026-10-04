import csv
import importlib.util
import json
import pathlib
import tempfile
import unittest
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


anki = load('anki', ROOT/'plugins/anki-builder/skills/exportar-anki-tsv/scripts/export_anki.py')
pack = load('pack', ROOT/'scripts/package_plugin.py')
audit = load('audit', ROOT/'scripts/validate_catalog.py')


class AnkiExport(unittest.TestCase):
    def test_unicode_html_multiline_source_and_tags(self):
        rows = anki.export([{'front':'O que é A < B?','back':'É uma comparação.\nLinha\t2','source':'Capítulo 1','tags':['python','básico']}], 'basic')
        self.assertEqual(rows[0], ('O que é A &lt; B?', 'É uma comparação.<br>Linha    2<br>Fonte: Capítulo 1', 'python básico'))
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp)/'cards.tsv'
            with path.open('w',encoding='utf-8',newline='') as stream:
                csv.writer(stream,delimiter='\t',lineterminator='\n').writerows(rows)
            with path.open(encoding='utf-8',newline='') as stream:
                self.assertEqual(list(csv.reader(stream,delimiter='\t')), [list(rows[0])])

    def test_cloze_preserves_syntax(self):
        text = 'A {{c1::chave primária}} é {{c2::única}}.'
        rows = anki.export([{'text':text,'extra':'SQL'}], 'cloze')
        self.assertEqual(rows[0], (text,'SQL',''))

    def test_invalid_cards_fail(self):
        cases = [([], 'basic'),([{'front':'x'}],'basic'),([{'front':'x','back':''}],'basic'),([{'front':'x','back':'y','tags':['duas palavras']}],'basic'),([{'text':'{{c0::inválido}}'}],'cloze'),([{'text':'{{c1::x}} {{'}],'cloze'),([{'front':'x','back':'a'},{'front':'x','back':'b'}],'basic')]
        for cards,model in cases:
            with self.subTest(cards=cards), self.assertRaises(ValueError):
                anki.export(cards,model)


class Packages(unittest.TestCase):
    def create(self, parent):
        folder = parent/'example'
        (folder/'skills/action').mkdir(parents=True)
        (folder/'.codex-plugin').mkdir()
        (folder/'plugin.json').write_text(json.dumps({'name':'example','version':'0.1.0'}))
        (folder/'skills/action/SKILL.md').write_text('Instructions')
        (folder/'.codex-plugin/plugin.json').write_text('{}')
        return folder

    def test_single_root_hidden_overlay_and_excluded_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = pathlib.Path(tmp)
            folder=self.create(base)
            (folder/'__pycache__').mkdir()
            (folder/'__pycache__/x.pyc').write_bytes(b'cache')
            result=pack.package(folder,base/'example.zip')
            self.assertEqual(len(result['sha256']),64)
            with zipfile.ZipFile(base/'example.zip') as archive:
                names=archive.namelist()
                self.assertIn('example/.codex-plugin/plugin.json',names)
                self.assertTrue(all(name.startswith('example/') for name in names))
                self.assertFalse(any('__pycache__' in name for name in names))

    def test_refuse_overwrite_inside_symlink_and_secret(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=pathlib.Path(tmp)
            folder=self.create(base)
            with self.assertRaises(ValueError):
                pack.package(folder,folder/'out.zip')
            output=base/'out.zip'
            output.write_bytes(b'existing')
            with self.assertRaises(ValueError):
                pack.package(folder,output)
            (folder/'link').symlink_to(base/'outside')
            with self.assertRaises(ValueError):
                pack.package(folder,base/'new.zip')
            (folder/'link').unlink()
            (folder/'.env').write_text('SECRET=not-a-real-secret')
            with self.assertRaises(ValueError):
                pack.package(folder,base/'new.zip')


class CatalogValidation(unittest.TestCase):
    def fixture(self,base):
        folder=base/'plugins/example'
        (folder/'skills/action').mkdir(parents=True)
        manifest={'name':'example','version':'0.1.0','description':'Example','extensions':{'com.openai':{'interface':{'shortDescription':'Example'}}}}
        (folder/'plugin.json').write_text(json.dumps(manifest))
        (folder/'README.md').write_text('Example')
        body='---\nname: action\ndescription: Use for example action\n---\n\n'+('Execute documented steps and verify results. '*4)
        (folder/'skills/action/SKILL.md').write_text(body)
        (base/'plugins-index.json').write_text(json.dumps({'plugins':[{'name':'example','version':'0.1.0','skills':['action']}]}))
        return folder

    def test_catalog_consistency_and_missing_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=pathlib.Path(tmp)
            folder=self.fixture(base)
            self.assertEqual(audit.validate(base)['errors'],[])
            skill=folder/'skills/action/SKILL.md'
            skill.write_text(skill.read_text()+'\nRead [guide](references/missing.md).\n')
            self.assertTrue(any('referência ausente' in error for error in audit.validate(base)['errors']))

    def test_divergent_index_and_overlay(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=pathlib.Path(tmp)
            folder=self.fixture(base)
            (folder/'.codex-plugin').mkdir()
            (folder/'.codex-plugin/plugin.json').write_text(json.dumps({'name':'example','version':'0.0.1'}))
            (base/'plugins-index.json').write_text(json.dumps({'plugins':[]}))
            errors=audit.validate(base)['errors']
            self.assertTrue(any('identidade/versão' in error for error in errors))
            self.assertTrue(any('divergentes do filesystem' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
