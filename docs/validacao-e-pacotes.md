# Validação e pacotes

## Verificação local

Requisitos: Python 3.10+ e PyYAML 6. As dependências de geração de documentos, imagens e gráficos dependem da tarefa e não são instaladas por estes pacotes.

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/generate_catalog.py --check
python3 scripts/validate_catalog.py
python3 scripts/check_links.py
python3 -m unittest discover -s tests -v
```

O validador local verifica nomes, versões, estrutura YAML, existência de referências Markdown, assets, links simbólicos, coerência dos overlays e catálogo. Retorna código diferente de zero para erros. Avisos de metadados antigos são separados de erros. Não valida o schema completo de cada cliente nem certifica o comportamento das skills.

Para validação no cliente, usar seu validador e testar exemplos com as ferramentas que estarão disponíveis na instalação. Não assumir que uma skill que usa navegação tem uma API própria.

O gerador lê manifestos, frontmatter das skills e `metadata/catalog.json`; `--check` retorna erro quando README, catálogo ou índice estiverem desatualizados. Sem `--check`, atualiza esses três arquivos. O verificador de links checa somente destinos locais, sem validar URLs externas ou âncoras. O GitHub executa esses checks pelo workflow de validação.

## Exportação Anki

Criar JSON para Basic:

```json
[
  {"front":"O que é uma chave primária?", "back":"Um identificador único de cada registro.", "tags":["sql", "basico"], "source":"Material fornecido, seção Chaves"}
]
```

Para Cloze:

```json
[
  {"text":"Uma chave {{c1::primária}} identifica cada registro.", "extra":"Deve ser única e não nula.", "tags":["sql"]}
]
```

```bash
python3 plugins/anki-builder/skills/exportar-anki-tsv/scripts/export_anki.py cards.json cards.tsv --model basic
python3 plugins/anki-builder/skills/exportar-anki-tsv/scripts/export_anki.py cloze.json cloze.tsv --model cloze
```

O TSV usa UTF-8, tabulação e não contém cabeçalho. O script valida campos, evita frentes duplicadas e não sobrescreve arquivo existente. Campos são escapados como HTML; quebras internas viram `<br>`. No Anki, selecionar modelo Basic ou Cloze conforme arquivo, permitir HTML e mapear campo 3 para Tags. O texto da fonte é anexado ao verso ou campo Extra. Não gera APKG nem sincroniza com a conta.

## Empacotamento

Após validar, usar:

```bash
python3 scripts/package_plugin.py plugins/datalab /caminho/de/saida/datalab.zip
```

A saída precisa estar fora da pasta do plugin e ainda não existir. O utilitário inclui uma única raiz, mantém arquivos ocultos de compatibilidade, exclui caches e recusa links simbólicos e nomes de arquivos secretos conhecidos. A detecção por nome não substitui revisão humana para credenciais embutidas no conteúdo. O resultado inclui SHA-256 e contagem de arquivos.

Gerar pacote não significa instalar, publicar ou conectar uma ferramenta. Para publicar um plugin em diretório público, seguir os requisitos atuais desse diretório separadamente.
