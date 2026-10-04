#!/usr/bin/env python3
"""Empacotar um plugin existente, excluindo caches e segredos conhecidos."""
import argparse
import hashlib
import json
import pathlib
import zipfile

EXCLUDED = {'.git', '__pycache__', 'node_modules', '.venv', '.pytest_cache', '.DS_Store'}


def package(folder, output):
    folder, output = folder.resolve(), output.resolve()
    manifest = json.loads((folder/'plugin.json').read_text())
    if manifest['name'] != folder.name:
        raise ValueError('O nome do manifesto precisa corresponder à pasta.')
    if output.is_relative_to(folder):
        raise ValueError('Gerar o arquivo fora da pasta do plugin.')
    if output.exists():
        raise ValueError('Saída existente; escolher outro caminho.')
    files = []
    for path in sorted(folder.rglob('*')):
        rel = path.relative_to(folder)
        if any(part in EXCLUDED for part in rel.parts):
            continue
        if path.is_symlink():
            raise ValueError(f'Link simbólico não permitido: {rel}')
        if not path.is_file():
            continue
        if path.name.startswith('.env') or path.suffix in {'.pem','.key','.p12','.pyc'} or path.name in {'credentials.json','secrets.json'}:
            raise ValueError(f'Remover arquivo potencialmente secreto: {rel}')
        files.append(path)
    if not any(path.name == 'SKILL.md' for path in files):
        raise ValueError('Nenhuma skill encontrada.')
    with zipfile.ZipFile(output, 'x', compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, folder.name+'/'+path.relative_to(folder).as_posix())
    with zipfile.ZipFile(output) as archive:
        if archive.testzip():
            raise ValueError('Arquivo ZIP corrompido.')
    return {'archive':str(output),'files':len(files),'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder',type=pathlib.Path)
    parser.add_argument('output',type=pathlib.Path)
    args=parser.parse_args()
    try:
        print(json.dumps(package(args.folder,args.output),ensure_ascii=False))
    except (ValueError,OSError,KeyError) as exc:
        parser.exit(1,f'Erro: {exc}\n')


if __name__ == '__main__':
    main()
