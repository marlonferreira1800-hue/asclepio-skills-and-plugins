#!/usr/bin/env python3
"""Conferir destinos locais de links Markdown; não acessar a rede."""
import argparse
import json
import pathlib
import re
import sys
from urllib.parse import unquote, urlsplit


def check(root):
    root=root.resolve()
    errors=[]
    checked=0
    for path in sorted(root.rglob('*.md')):
        if any(part in {'.git','node_modules','.venv','__pycache__'} for part in path.relative_to(root).parts):
            continue
        text=path.read_text(encoding='utf-8')
        # Não interpretar exemplos de sintaxe dentro de blocos de código.
        text=re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '',text,flags=re.MULTILINE|re.DOTALL)
        for match in re.finditer(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)',text):
            target=match.group(1).strip('<>')
            parts=urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            destination=(path.parent/unquote(parts.path)).resolve()
            checked+=1
            if not destination.is_relative_to(root):
                errors.append({'file':str(path.relative_to(root)),'target':target,'error':'Destino fora do repositório'})
            elif not destination.exists():
                errors.append({'file':str(path.relative_to(root)),'target':target,'error':'Destino inexistente'})
    return {'local_links_checked':checked,'errors':errors,'scope':'Destinos locais; URLs externas e âncoras não são verificadas.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',nargs='?',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1])
    args=parser.parse_args()
    result=check(args.root)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    sys.exit(bool(result['errors']))


if __name__ == '__main__':
    main()
