# Asclépio — Skills & Plugins para Agentes de IA

Coleção modular para estudo, dados, pesquisa, produtividade e criação. Desenvolvida por Marlon Ferreira.

**28 plugins e 94 skills** disponíveis como código-fonte. Cada pacote possui manifesto, instruções e exemplos; ferramentas e conexões dependem do cliente.

## Catálogo

| Plugin | Skills | Função |
|---|---:|---|
| [Anki Builder](plugins/anki-builder) | 4 | Criar flashcards básicos, cloze e exportação TSV com origem rastreável. |
| [API Explorer](plugins/api-explorer) | 4 | Ler documentação, realizar consultas autorizadas, paginar resultados e documentar respostas. |
| [Artigo Crítico](plugins/artigo-critico) | 4 | Avaliar desenho, vieses, estatísticas e aplicabilidade de pesquisas. |
| [Carreira Lab](plugins/carreira-lab) | 4 | Adaptar currículo, revisar perfil, praticar entrevista e mapear evidências de competências. |
| [Cognitus](plugins/cognitus) | 1 | Mentor de aprendizagem ativa que desenvolve raciocínio, retenção e autonomia com método socrático, Feynman, prática deliberada e repetição espaçada. |
| [Comparador de carros](plugins/comparador-precos-carros) | 4 | Pesquisa e compara preços de carros no Brasil por categoria, marca, modelo, versão e região, com fontes e critérios claros. |
| [Dados de Saúde Brasil](plugins/dados-saude-brasil) | 4 | Consulta simples a dados públicos de doenças no Brasil usando fontes oficiais do SUS. |
| [Dashboard Studio](plugins/dashboard-studio) | 4 | Definir indicadores, modelagem, layout e medidas DAX para dashboards. |
| [DataLab — Análise de Dados](plugins/datalab) | 4 | Limpar bases, explorar dados, construir gráficos e produzir relatórios reproduzíveis. |
| [Documento Studio](plugins/documento-studio) | 4 | Criar relatórios, formatar documentos, preparar apresentações e revisar PDFs. |
| [Edital Fácil](plugins/edital-facil) | 5 | Lê editais de concursos e seleções e transforma requisitos, etapas, salários e prazos em um resumo e checklist prático. |
| [GitHub Organizer](plugins/github-organizer) | 4 | Melhorar README, gerar catálogo, registrar mudanças e conferir links. |
| [InvestIA — Análise de Investimentos](plugins/investia) | 4 | Pesquisa e compara investimentos com fundamentos, notícias, cenários e simulação de risco usando ferramentas disponíveis no ChatGPT. |
| [LinkedIn Conteúdo Diário](plugins/linkedin-conteudo-diario) | 1 | Cria, valida e agenda lotes diários de posts educativos com imagens para LinkedIn. |
| [MedQuest — Medicina por Questões](plugins/medquest) | 4 | Treino ativo de Medicina por questões, casos clínicos e correção comentada. |
| [MedTermo AI](plugins/medtermo-ai) | 1 | Jogo de adivinhação diagnóstica com cinco tentativas, pistas progressivas e revisão para provas de residência médica. |
| [Mentor de Estudos](plugins/mentor-de-estudos) | 1 | Tutor pessoal para planejar estudos, explicar conteúdos, praticar, revisar e acompanhar o progresso do estudante. |
| [Pesquisa Científica](plugins/pesquisa-cientifica) | 4 | Buscar literatura, extrair evidências, comparar estudos e organizar referências. |
| [Plugin Builder](plugins/plugin-builder) | 4 | Estruturar plugins de skills, preparar manifestos, documentar requisitos e empacotar versões. |
| [PostLab — Designer Criativo](plugins/postlab) | 5 | Designer de posts criativos com artes, fotos, legendas e carrosséis para redes sociais. |
| [ProvaLab](plugins/provalab) | 1 | Cria avaliações e cadernos de questões a partir de apostilas, slides, guias e materiais enviados pelo usuário. |
| [Python Lab](plugins/python-lab) | 4 | Explicar código, depurar erros, criar exercícios e organizar projetos Python. |
| [Residência Radar Brasil](plugins/residencia-radar-brasil) | 5 | Pesquisa e compara vagas, editais, concorrência, notas e chamadas de programas de residência médica no Brasil. |
| [Resumo Visual Manuscrito](plugins/resumo-visual-manuscrito) | 1 | Transforma qualquer tema ou material de estudo em um resumo visual manuscrito, didático, organizado e focado em revisão de prova. |
| [Skill Auditor](plugins/skill-auditor) | 4 | Avaliar estrutura, instruções, recursos e comportamento de skills com casos de uso. |
| [SQL Mentor](plugins/sql-mentor) | 4 | Ensinar, escrever, depurar e praticar SQL com exemplos controlados. |
| [TokenMeter Universal](plugins/tokenmeter-universal) | 1 | Registro portátil de consumo de tokens com relatórios diários, semanais, mensais, anuais e total acumulado. Importação de metadados, custos configuráveis e MCP local. |
| [VisualExplain](plugins/visualexplain) | 4 | Esqueleto para transformar materiais em explicações visuais animadas com roteiro e HTML. |

## Uso e instalação

Cada pasta `plugins/<nome>` contém um pacote independente. O manifesto raiz segue Agent Plugins 1.0; `.codex-plugin/plugin.json` conserva o overlay usado neste projeto. As skills estão em `skills/<nome>/SKILL.md`.

Para um cliente que aceite skills, use o mecanismo de instalação documentado por ele e selecione a pasta da skill. Para importar um plugin no ChatGPT/Codex, use o fluxo de plugins suportado pela sua versão. Estes arquivos no GitHub **não instalam nem atualizam automaticamente plugins da sua conta**. A compatibilidade de manifests e recursos deve ser validada pelo cliente de destino.

Não há um novo servidor MCP nos pacotes desta ampliação. Navegação, execução de Python, geração de imagens, criação de documentos e conexão a banco de dados precisam estar disponíveis no assistente; cada README explica as dependências.

## Ampliação de outubro de 2026

Foram adicionadas 79 skills para os 15 conjuntos propostos e para PostLab, VisualExplain, MedQuest, Dados de Saúde Brasil, InvestIA e Comparador de Carros. Edital Fácil e Residência Radar Brasil foram ampliados; o nome Residência Explorer foi incorporado ao Radar para manter sua identidade. A versão existente do VisualExplain foi incluída no repositório junto com suas novas skills.

- [Mapa completo das novas skills](docs/novas-skills.md)
- [Como validar e empacotar](docs/validacao-e-pacotes.md)
- [Histórico de mudanças](CHANGELOG.md)

## Utilitários

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_catalog.py
python3 scripts/package_plugin.py plugins/datalab /caminho/fora-do-plugin/datalab.zip
```

O Anki Builder inclui exportador TSV, documentado em sua skill `exportar-anki-tsv`. Scripts funcionam localmente e não incluem tokens ou conexão automática a serviços.

## Qualidade e limites

- Distinguir análise executada de código ou roteiro apenas preparado.
- Usar fontes oficiais e registrar edição, período e data em pesquisas atuais.
- Não substituir dados ausentes por números inventados.
- Não publicar conteúdo nem enviar dados a terceiros sem pedido específico.
- Os checks locais conferem estrutura e consistência; não certificam todos os comportamentos nem garantem importação em cada cliente.

## Licença

[MIT](LICENSE). O conteúdo novo desta ampliação foi escrito para este projeto; os repositórios pesquisados serviram como referência de organização, sem importar suas coleções. Recursos de terceiros já existentes mantêm seus avisos e condições.
