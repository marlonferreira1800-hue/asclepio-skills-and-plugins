#!/usr/bin/env python3
"""Gerar navegação e índice a partir dos pacotes e metadata/catalog.json."""
import argparse
import json
import pathlib
import sys
import yaml


def md(value):
    return str(value).replace('\n', ' ').replace('|', '\\|')


def read_skill(path):
    chunks = path.read_text(encoding='utf-8').split('---', 2)
    if len(chunks) != 3 or chunks[0].strip():
        raise ValueError(f'{path}: frontmatter ausente')
    data = yaml.safe_load(chunks[1])
    if not isinstance(data, dict) or not data.get('name') or not data.get('description'):
        raise ValueError(f'{path}: name/description ausentes')
    if data['name'] != path.parent.name:
        raise ValueError(f'{path}: nome divergente da pasta')
    return data


def build(root):
    config = json.loads((root/'metadata/catalog.json').read_text(encoding='utf-8'))
    actual = {path.parent.name:path for path in (root/'plugins').glob('*/plugin.json')}
    seen, group_ids, rows, details = set(), set(), [], {}
    for group in config['groups']:
        if group['id'] in group_ids:
            raise ValueError(f'Área repetida: {group["id"]}')
        group_ids.add(group['id'])
        for entry in group['plugins']:
            name = entry['name']
            if name in seen:
                raise ValueError(f'Plugin repetido nas áreas: {name}')
            if name not in actual:
                raise ValueError(f'Plugin sem manifesto: {name}')
            seen.add(name)
            manifest = json.loads(actual[name].read_text(encoding='utf-8'))
            if manifest['name'] != name:
                raise ValueError(f'Identidade divergente: {name}')
            ui = manifest.get('extensions',{}).get('com.openai',{}).get('interface',{})
            skills = [read_skill(path) for path in sorted((actual[name].parent/'skills').glob('*/SKILL.md'))]
            names = [skill['name'] for skill in skills]
            if entry['primarySkill'] not in names:
                raise ValueError(f'Skill principal ausente: {name}/{entry["primarySkill"]}')
            details[name] = skills
            rows.append(dict(name=name,displayName=ui.get('displayName',name),version=manifest['version'],category=ui.get('category','Productivity'),group=group['id'],skill=entry['primarySkill'],description=manifest['description'],path='plugins/'+name,skills=names))
    if seen != set(actual):
        raise ValueError('Plugins sem área: '+', '.join(sorted(set(actual)-seen)))
    index={key:config[key] for key in ('name','version','description','author')}
    index['plugins']=sorted(rows,key=lambda row:row['name'])
    total=sum(len(row['skills']) for row in rows)
    byname={row['name']:row for row in rows}
    generated='<!-- Gerado por scripts/generate_catalog.py. Editar manifestos, skills ou metadata/catalog.json. -->'
    readme=[generated,'','# Asclépio — Skills & Plugins para Agentes de IA','','**'+str(len(rows))+' plugins · '+str(total)+' skills · '+str(len(config['groups']))+' áreas**','','Uma coleção em português para aprender, pesquisar, analisar dados e criar conteúdo com agentes de IA. Desenvolvida por Marlon Ferreira.','','[Começar a usar](docs/guia-rapido.md) · [Todas as skills](docs/catalogo.md) · [Documentação](docs/README.md) · [Contribuir](CONTRIBUTING.md)','','## Explore por área','','| Área | Plugins | Skills |','|---|---|---:|']
    for group in config['groups']:
        plugins=[byname[e['name']] for e in group['plugins']]
        links=', '.join(f'[{md(p["displayName"])}]({p["path"]})' for p in plugins)
        readme.append(f'| [{md(group["title"])}](docs/catalogo.md#{group["id"]}) | {links} | {sum(len(p["skills"]) for p in plugins)} |')
    readme += ['','## Escolha um ponto de partida','','| Quero… | Começar por |','|---|---|','| Aprender ou praticar Medicina | [MedQuest](plugins/medquest) |','| Analisar uma planilha | [DataLab](plugins/datalab) |','| Aprender SQL ou Python | [SQL Mentor](plugins/sql-mentor) ou [Python Lab](plugins/python-lab) |','| Ler artigos com atenção aos métodos | [Pesquisa Científica](plugins/pesquisa-cientifica) e [Artigo Crítico](plugins/artigo-critico) |','| Transformar material em cartões | [Anki Builder](plugins/anki-builder) |','| Criar posts ou aulas visuais | [PostLab](plugins/postlab) e [VisualExplain](plugins/visualexplain) |','| Criar e revisar meus plugins | [Plugin Builder](plugins/plugin-builder) e [Skill Auditor](plugins/skill-auditor) |','','## Como os pacotes funcionam','','Cada pasta em `plugins/` é um pacote independente. Ela reúne um manifesto `plugin.json`, documentação e skills em `skills/<nome>/SKILL.md`. Algumas também incluem scripts, assets ou configuração MCP.','','As skills orientam o agente; sua execução depende das ferramentas disponíveis no cliente. Consultas atuais precisam de navegação, código precisa de runtime e arquivos como PBIX dependem do aplicativo apropriado. Confira o README de cada pacote. Os arquivos do GitHub não instalam nem conectam automaticamente plugins da sua conta.','','## Estrutura','','| Pasta ou arquivo | Finalidade |','|---|---|','| `plugins/` | Pacotes independentes e suas skills |','| `docs/` | Guias, catálogo completo e registros de verificação |','| `metadata/catalog.json` | Áreas e skill principal de cada pacote |','| `plugins-index.json` | Índice gerado para ferramentas |','| `scripts/` | Geração, validação, links e empacotamento |','| `tests/` | Testes dos utilitários do catálogo |','| `.github/workflows/` | Verificações automáticas |','','## Desenvolvimento','','```bash','python3 -m pip install -r requirements-dev.txt','python3 scripts/generate_catalog.py --check','python3 scripts/validate_catalog.py','python3 scripts/check_links.py','python3 -m unittest discover -s tests -v','```','','Após alterar pacotes ou áreas, executar `python3 scripts/generate_catalog.py` para atualizar o README, catálogo e índice. Confira [como contribuir](CONTRIBUTING.md).','','## Licença e mudanças','','[Licença MIT](LICENSE) · [Histórico de mudanças](CHANGELOG.md). Recursos de terceiros mantêm seus avisos e condições.','']
    full=[generated,'','# Catálogo de plugins e skills','',f'{len(rows)} plugins e {total} skills. Os nomes abaixo são os identificadores reais dos arquivos. Para exemplos e dependências, abra o README de cada plugin.','','[Voltar ao início](../README.md) · [Guia rápido](guia-rapido.md)','']
    for group in config['groups']:
        # Heading ASCII separado mantém a âncora estável entre renderizadores.
        full += ['## '+group['id'],'','**'+group['title']+'**','']
        for entry in group['plugins']:
            row=byname[entry['name']]
            full += [f'### {row["displayName"]}','',f'[Documentação do plugin](../{row["path"]}/README.md) · Versão `{row["version"]}`','',row['description'],'','| Skill | Quando usar |','|---|---|']
            for s in details[row['name']]:
                path='../'+row['path']+'/skills/'+s['name']+'/SKILL.md'
                full.append(f'| [`{s["name"]}`]({path}) | {md(s["description"])} |')
            full.append('')
    return {'README.md':'\n'.join(readme),'plugins-index.json':json.dumps(index,ensure_ascii=False,indent=2)+'\n','docs/catalogo.md':'\n'.join(full)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1])
    parser.add_argument('--check',action='store_true',help='Conferir sem escrever arquivos')
    args=parser.parse_args()
    try:
        outputs=build(args.root)
        stale=[]
        for name,content in outputs.items():
            path=args.root/name
            if args.check:
                if not path.exists() or path.read_text(encoding='utf-8') != content:
                    stale.append(name)
            else:
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text(content,encoding='utf-8')
        if stale:
            print('Catálogo desatualizado: '+', '.join(stale),file=sys.stderr)
            return 1
        print('Catálogo conferido.' if args.check else 'README, índice e catálogo atualizados.')
        return 0
    except (ValueError,KeyError,OSError,yaml.YAMLError) as exc:
        print(f'Erro: {exc}',file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
