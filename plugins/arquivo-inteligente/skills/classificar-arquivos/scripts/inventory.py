#!/usr/bin/env python3
"""Inventário somente leitura; hashes opcionais confirmam conteúdo idêntico."""
import argparse
import hashlib
import json
import os
from pathlib import Path

EXCLUDE = {'.git', '.venv', 'node_modules', '__pycache__'}

def inventory(root, with_hash=False, output=None):
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError('A raiz deve ser uma pasta existente')
    rows, skipped, errors = [], [], []
    def failed(exc):
        errors.append({'path': str(exc.filename), 'error': str(exc)})
    for folder, dirs, names in os.walk(root, followlinks=False, onerror=failed):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDE and not (Path(folder)/d).is_symlink())
        for name in sorted(names):
            path = Path(folder)/name
            rel = str(path.relative_to(root))
            if path.is_symlink() or name == '.env' or name.startswith('.env.') or name in {'credentials.json', 'id_rsa', 'id_ed25519'} or (output and path.resolve() == Path(output).resolve()):
                skipped.append(rel)
                continue
            try:
                before = path.stat()
                row = {'path': rel, 'suffix': path.suffix.lower(), 'size': before.st_size}
                if with_hash:
                    digest = hashlib.sha256()
                    with path.open('rb') as stream:
                        for chunk in iter(lambda: stream.read(1024*1024), b''):
                            digest.update(chunk)
                    after = path.stat()
                    if (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
                        raise ValueError('Arquivo mudou durante o cálculo do hash')
                    row['sha256'] = digest.hexdigest()
                rows.append(row)
            except (OSError, ValueError) as exc:
                errors.append({'path': rel, 'error': str(exc)})
    groups = {}
    for row in rows:
        if 'sha256' in row:
            groups.setdefault((row['size'], row['sha256']), []).append(row['path'])
    return {'root': str(root), 'files': rows, 'duplicates': [v for v in groups.values() if len(v)>1], 'skipped': skipped, 'errors': errors}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', required=True, type=Path)
    p.add_argument('--output', required=True, type=Path)
    p.add_argument('--hash', action='store_true', dest='with_hash')
    a = p.parse_args()
    try:
        if a.output.exists():
            raise ValueError('A saída já existe')
        result = inventory(a.root, a.with_hash, a.output)
        with a.output.open('x', encoding='utf-8') as stream:
            json.dump(result, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
    except (OSError, ValueError) as exc:
        p.exit(1, str(exc)+'\n')

if __name__ == '__main__':
    main()
