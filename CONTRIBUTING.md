# Como contribuir

## Organização dos pacotes

Manter cada plugin em `plugins/<nome>`, com nome em minúsculas e hífens. Preservar os caminhos e identificadores dos plugins existentes para evitar quebrar instalações e referências.

| Arquivo | Regra |
|---|---|
| `plugin.json` | Manifesto portátil e versão do pacote |
| `.codex-plugin/plugin.json` | Overlay opcional, com a mesma identidade e versão |
| `README.md` do plugin | Propósito, requisitos, exemplos e limitações |
| `skills/<nome>/SKILL.md` | Frontmatter com `name` e `description`, seguido de instruções |
| `skills/<nome>/agents/openai.yaml` | Metadados de interface quando utilizados |
| `scripts/`, `references/`, `assets/` dentro de uma skill | Somente recursos realmente usados |

Não incluir credenciais, ambientes virtuais, caches, arquivos pessoais ou dependências vendorizadas. Manter termos e licença de recursos de terceiros.

## Adicionar ou ampliar um plugin

1. Ler as instruções existentes e verificar se o objetivo já pertence a um pacote.
2. Criar skills com gatilhos e resultados distintos, incluindo entradas, procedimento, falhas e exemplo.
3. Documentar as ferramentas necessárias. Não declarar uma API, editor ou servidor que não está implementado.
4. Ao adicionar pacote, cadastrá-lo uma única vez em `metadata/catalog.json` e definir `primarySkill` existente.
5. Ao mudar pacote, atualizar sua versão e overlays sem renomear a identidade. O catálogo tem uma versão independente dos plugins.
6. Gerar índice e documentação e rodar os checks abaixo.

## Fonte dos arquivos gerados

`README.md`, `plugins-index.json` e `docs/catalogo.md` são gerados por `scripts/generate_catalog.py`. Não editar esses arquivos diretamente. As descrições e versões vêm dos manifestos; nomes e descrições das skills vêm de `SKILL.md`; áreas e skill principal vêm de `metadata/catalog.json`.

O campo legado `skill` do índice continua presente; `skills` contém a lista completa. O índice também inclui `group` para navegação por área.

## Verificações

Requisitos: Python 3.10+ e dependências de desenvolvimento.

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/generate_catalog.py
python3 scripts/generate_catalog.py --check
python3 scripts/validate_catalog.py
python3 scripts/check_links.py
python3 -m unittest discover -s tests -v
git diff --check
```

Testar scripts novos com entrada válida, limite e erro relevante. Avaliar pelo menos um exemplo concreto de workflows que mudarem substancialmente. Não declarar todas as skills funcionalmente testadas quando só a estrutura foi conferida.

O workflow do GitHub executa essas verificações em push e pull request. O verificador de links não acessa a rede e não valida âncoras. O validador local não substitui o schema completo nem a importação no cliente.

## Pull requests

Descrever o problema, a nova entrega, os pacotes afetados, os testes executados e limitações. Atualizar [CHANGELOG.md](CHANGELOG.md) para mudanças relevantes. Manter alterações pequenas quando possível e não alterar arquivos de outros plugins sem motivo.
