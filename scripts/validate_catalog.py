#!/usr/bin/env python3
"""Validar invariantes locais de plugins; não substitui schemas dos clientes."""
import argparse
import json
import pathlib
import re
import sys
import yaml

NAME = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


def validate(root):
    errors, warnings = [], []
    plugin_rows = []
    skills_count = 0
    for folder in sorted((root / 'plugins').iterdir()):
        manifest_path = folder / 'plugin.json'
        if not manifest_path.is_file():
            continue
        try:
            manifest = json.loads(manifest_path.read_text())
            name, version = manifest['name'], manifest['version']
            if name != folder.name or not NAME.fullmatch(name) or len(name) > 64:
                errors.append(f'{manifest_path}: nome inválido ou diferente da pasta')
            if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?', version):
                errors.append(f'{manifest_path}: versão inválida')
            if not manifest.get('description'):
                errors.append(f'{manifest_path}: descrição ausente')
            interface = manifest.get('extensions', {}).get('com.openai', {}).get('interface', {})
            if len(interface.get('shortDescription', '')) > 30:
                errors.append(f'{manifest_path}: shortDescription excede 30 caracteres')
            for prohibited in ('skills', 'mcpServers', 'apps', 'interface'):
                if prohibited in manifest:
                    errors.append(f'{manifest_path}: campo portable proibido: {prohibited}')
            for key in ('logo', 'composerIcon', 'logoDark', 'composerIconDark'):
                value = interface.get(key)
                if value:
                    resolved = (folder/value).resolve()
                    if not resolved.is_relative_to(folder.resolve()) or not resolved.is_file():
                        errors.append(f'{manifest_path}: asset inválido: {value}')
            for overlay_path in (folder/'.codex-plugin/plugin.json', folder/'.claude-plugin/plugin.json'):
                if overlay_path.exists():
                    overlay = json.loads(overlay_path.read_text())
                    if overlay.get('name') != name or overlay.get('version') != version:
                        errors.append(f'{overlay_path}: identidade/versão divergente')
            names = []
            for skill in sorted((folder/'skills').glob('*/SKILL.md')):
                text = skill.read_text(encoding='utf-8')
                chunks = text.split('---', 2)
                if len(chunks) != 3 or chunks[0].strip():
                    errors.append(f'{skill}: frontmatter ausente')
                    continue
                header = yaml.safe_load(chunks[1])
                if not isinstance(header, dict):
                    errors.append(f'{skill}: frontmatter não é objeto')
                    continue
                skill_name = header.get('name', '')
                if not NAME.fullmatch(skill_name) or len(skill_name)>64 or skill_name != skill.parent.name:
                    errors.append(f'{skill}: nome inválido ou diferente da pasta')
                if not isinstance(header.get('description'), str) or not header['description'].strip():
                    errors.append(f'{skill}: descrição ausente')
                if len(chunks[2].strip()) < 100:
                    errors.append(f'{skill}: instruções insuficientes')
                if re.search(r'\bTODO\b|\[INSERT', text):
                    errors.append(f'{skill}: placeholder pendente')
                for target in re.findall(r'\]\(([^)]+)\)', chunks[2]):
                    if '://' in target or target.startswith('#'):
                        continue
                    target = target.split('#')[0]
                    if target and not (skill.parent/target).exists():
                        errors.append(f'{skill}: referência ausente: {target}')
                agent = skill.parent/'agents/openai.yaml'
                if agent.exists():
                    metadata = yaml.safe_load(agent.read_text())
                    prompt = metadata.get('interface', {}).get('default_prompt', '')
                    if '$'+skill_name not in prompt:
                        warnings.append(f'{agent}: prompt não menciona $nome (legado)')
                names.append(skill_name)
                skills_count += 1
            if not names:
                errors.append(f'{folder}: plugin sem skills')
            # Não exigir README para skills; somente para plugin.
            if not (folder/'README.md').is_file():
                warnings.append(f'{folder}: README de plugin ausente')
            for file in folder.rglob('*'):
                if file.is_symlink():
                    errors.append(f'{file}: link simbólico no pacote')
            plugin_rows.append({'name':name,'version':version,'skills':names,'path':str(folder.relative_to(root))})
        except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as exc:
            errors.append(f'{manifest_path}: {exc}')
    index_path = root/'plugins-index.json'
    if index_path.exists():
        try:
            index = json.loads(index_path.read_text())
            indexed = {p['name']:p for p in index['plugins']}
            actual = {p['name']:p for p in plugin_rows}
            if set(indexed) != set(actual):
                errors.append('plugins-index.json: plugins divergentes do filesystem')
            for name in set(indexed) & set(actual):
                if indexed[name]['version'] != actual[name]['version'] or indexed[name].get('skills') != actual[name]['skills']:
                    errors.append(f'plugins-index.json: versão/skills divergentes em {name}')
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f'plugins-index.json: {exc}')
    return {'plugins':len(plugin_rows),'skills':skills_count,'errors':errors,'warnings':warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = validate(args.root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(bool(result['errors']))


if __name__ == '__main__':
    main()
