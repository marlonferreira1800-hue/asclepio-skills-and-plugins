import importlib.util
import json
import pathlib
import tempfile
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


generator=load('generator',ROOT/'scripts/generate_catalog.py')
links=load('links',ROOT/'scripts/check_links.py')


class CatalogGeneration(unittest.TestCase):
    def fixture(self,root):
        (root/'metadata').mkdir()
        config={'name':'collection','version':'1.0.0','description':'Collection','author':{'name':'Example'},'groups':[{'id':'test','title':'Teste','plugins':[{'name':'example','primarySkill':'action'}]}]}
        (root/'metadata/catalog.json').write_text(json.dumps(config))
        plugin=root/'plugins/example'
        (plugin/'skills/action').mkdir(parents=True)
        (plugin/'plugin.json').write_text(json.dumps({'name':'example','version':'0.1.0','description':'Example','extensions':{'com.openai':{'interface':{'displayName':'Example'}}}}))
        (plugin/'skills/action/SKILL.md').write_text('---\nname: action\ndescription: "Use para A | B"\n---\n\nExecute steps.')
        return config,plugin

    def test_deterministic_generation_and_full_skill_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp)
            self.fixture(root)
            outputs=generator.build(root)
            self.assertEqual(outputs,generator.build(root))
            index=json.loads(outputs['plugins-index.json'])
            self.assertEqual(index['plugins'][0]['skill'],'action')
            self.assertEqual(index['plugins'][0]['skills'],['action'])
            self.assertEqual(index['plugins'][0]['group'],'test')
            self.assertIn('../plugins/example/skills/action/SKILL.md',outputs['docs/catalogo.md'])
            self.assertIn('A \\| B',outputs['docs/catalogo.md'])

    def test_duplicate_mapping_missing_primary_and_unlisted_plugin_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp)
            config,plugin=self.fixture(root)
            config['groups'][0]['plugins'].append({'name':'example','primarySkill':'action'})
            path=root/'metadata/catalog.json'
            path.write_text(json.dumps(config))
            with self.assertRaisesRegex(ValueError,'repetido'):
                generator.build(root)
            config['groups'][0]['plugins']=[{'name':'example','primarySkill':'missing'}]
            path.write_text(json.dumps(config))
            with self.assertRaisesRegex(ValueError,'principal ausente'):
                generator.build(root)
            config['groups'][0]['plugins']=[]
            path.write_text(json.dumps(config))
            with self.assertRaisesRegex(ValueError,'sem área'):
                generator.build(root)


class LocalLinks(unittest.TestCase):
    def test_relative_links_code_examples_and_external_urls(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp)
            (root/'docs').mkdir()
            (root/'target.md').write_text('Target')
            (root/'docs/guide.md').write_text('[OK](../target.md#anchor)\n[Externo](https://example.com)\n```markdown\n[Exemplo](missing.md)\n```\n')
            result=links.check(root)
            self.assertEqual(result['errors'],[])
            self.assertEqual(result['local_links_checked'],1)

    def test_missing_and_outside_destinations_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp)
            (root/'README.md').write_text('[Falta](missing.md)\n[Fora](../outside.md)\n')
            self.assertEqual(len(links.check(root)['errors']),2)


if __name__ == '__main__':
    unittest.main()
