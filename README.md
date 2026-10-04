<!-- Gerado por scripts/generate_catalog.py. Editar manifestos, skills ou metadata/catalog.json. -->

# Asclépio — Skills & Plugins para Agentes de IA

**39 plugins · 150 skills · 8 áreas**

Uma coleção em português para aprender, pesquisar, analisar dados e criar conteúdo com agentes de IA. Desenvolvida por Marlon Ferreira.

[Começar a usar](docs/guia-rapido.md) · [Todas as skills](docs/catalogo.md) · [Documentação](docs/README.md) · [Contribuir](CONTRIBUTING.md)

## Explore por área

| Área | Plugins | Skills |
|---|---|---:|
| [Medicina e residência](docs/catalogo.md#medicina) | [MedQuest — Medicina por Questões](plugins/medquest), [MedTermo AI](plugins/medtermo-ai), [Residência Radar Brasil](plugins/residencia-radar-brasil) | 10 |
| [Estudos e aprendizagem](docs/catalogo.md#estudos) | [Cognitus](plugins/cognitus), [Mentor de Estudos](plugins/mentor-de-estudos), [ProvaLab](plugins/provalab), [Anki Builder](plugins/anki-builder) | 7 |
| [Dados e programação](docs/catalogo.md#dados) | [DataLab — Análise de Dados](plugins/datalab), [SQL Mentor](plugins/sql-mentor), [Python Lab](plugins/python-lab), [Dashboard Studio](plugins/dashboard-studio) | 20 |
| [Pesquisa e saúde pública](docs/catalogo.md#pesquisa) | [Pesquisa Científica](plugins/pesquisa-cientifica), [Artigo Crítico](plugins/artigo-critico), [Dados de Saúde Brasil](plugins/dados-saude-brasil), [Projeto Científico](plugins/projeto-cientifico), [Bioestatística Lab](plugins/bioestatistica-lab), [Ensaios Clínicos Radar](plugins/ensaios-clinicos-radar), [Imagem Médica Lab](plugins/imagem-medica-lab), [Genômica Explorer](plugins/genomica-explorer) | 32 |
| [Design, documentos e conteúdo](docs/catalogo.md#criacao) | [PostLab — Designer Criativo](plugins/postlab), [LinkedIn Conteúdo Diário](plugins/linkedin-conteudo-diario), [Resumo Visual Manuscrito](plugins/resumo-visual-manuscrito), [VisualExplain](plugins/visualexplain), [Documento Studio](plugins/documento-studio) | 19 |
| [Carreira, concursos e organização](docs/catalogo.md#carreira) | [Carreira Lab](plugins/carreira-lab), [Edital Fácil](plugins/edital-facil), [Arquivo Inteligente](plugins/arquivo-inteligente), [Reunião Clara](plugins/reuniao-clara) | 17 |
| [Plugins, GitHub e APIs](docs/catalogo.md#desenvolvimento) | [GitHub Organizer](plugins/github-organizer), [Skill Auditor](plugins/skill-auditor), [Plugin Builder](plugins/plugin-builder), [API Explorer](plugins/api-explorer), [Projeto do Zero](plugins/projeto-do-zero), [Debug Investigador](plugins/debug-investigador), [Release Manager](plugins/release-manager) | 32 |
| [Finanças e comparações](docs/catalogo.md#financas) | [InvestIA — Análise de Investimentos](plugins/investia), [Comparador de carros](plugins/comparador-precos-carros), [TokenMeter Universal](plugins/tokenmeter-universal), [Recibos & Despesas](plugins/recibos-despesas) | 13 |

## Escolha um ponto de partida

| Quero… | Começar por |
|---|---|
| Aprender ou praticar Medicina | [MedQuest](plugins/medquest) |
| Analisar uma planilha | [DataLab](plugins/datalab) |
| Aprender SQL ou Python | [SQL Mentor](plugins/sql-mentor) ou [Python Lab](plugins/python-lab) |
| Ler artigos com atenção aos métodos | [Pesquisa Científica](plugins/pesquisa-cientifica) e [Artigo Crítico](plugins/artigo-critico) |
| Transformar material em cartões | [Anki Builder](plugins/anki-builder) |
| Criar posts ou aulas visuais | [PostLab](plugins/postlab) e [VisualExplain](plugins/visualexplain) |
| Criar e revisar meus plugins | [Plugin Builder](plugins/plugin-builder) e [Skill Auditor](plugins/skill-auditor) |

## Como os pacotes funcionam

Cada pasta em `plugins/` é um pacote independente. Ela reúne um manifesto `plugin.json`, documentação e skills em `skills/<nome>/SKILL.md`. Algumas também incluem scripts, assets ou configuração MCP.

As skills orientam o agente; sua execução depende das ferramentas disponíveis no cliente. Consultas atuais precisam de navegação, código precisa de runtime e arquivos como PBIX dependem do aplicativo apropriado. Confira o README de cada pacote. Os arquivos do GitHub não instalam nem conectam automaticamente plugins da sua conta.

## Estrutura

| Pasta ou arquivo | Finalidade |
|---|---|
| `plugins/` | Pacotes independentes e suas skills |
| `docs/` | Guias, catálogo completo e registros de verificação |
| `metadata/catalog.json` | Áreas e skill principal de cada pacote |
| `plugins-index.json` | Índice gerado para ferramentas |
| `scripts/` | Geração, validação, links e empacotamento |
| `tests/` | Testes dos utilitários do catálogo |
| `.github/workflows/` | Verificações automáticas |

## Desenvolvimento

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/generate_catalog.py --check
python3 scripts/validate_catalog.py
python3 scripts/check_links.py
python3 -m unittest discover -s tests -v
```

Após alterar pacotes ou áreas, executar `python3 scripts/generate_catalog.py` para atualizar o README, catálogo e índice. Confira [como contribuir](CONTRIBUTING.md).

## Licença e mudanças

[Licença MIT](LICENSE) · [Histórico de mudanças](CHANGELOG.md). Recursos de terceiros mantêm seus avisos e condições.
