<!-- Gerado por scripts/generate_catalog.py. Editar manifestos, skills ou metadata/catalog.json. -->

# Catálogo de plugins e skills

33 plugins e 111 skills. Os nomes abaixo são os identificadores reais dos arquivos. Para exemplos e dependências, abra o README de cada plugin.

[Voltar ao início](../README.md) · [Guia rápido](guia-rapido.md)

## medicina

**Medicina e residência**

### MedQuest — Medicina por Questões

[Documentação do plugin](../plugins/medquest/README.md) · Versão `0.2.1`

Treino ativo de Medicina por questões, casos clínicos e correção comentada.

| Skill                                                                                              | Quando usar                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`analisar-erros-estudo`](../plugins/medquest/skills/analisar-erros-estudo/SKILL.md)               | Use para interpretar respostas de simulados e orientar revisão específica.                                                                                                                        |
| [`classificar-questoes-medicas`](../plugins/medquest/skills/classificar-questoes-medicas/SKILL.md) | Use para organizar questões por tema, habilidade e nível cognitivo.                                                                                                                               |
| [`criar-prova-equivalente`](../plugins/medquest/skills/criar-prova-equivalente/SKILL.md)           | Use para gerar nova versão de prova preservando objetivos e distribuição.                                                                                                                         |
| [`questoes-medicina`](../plugins/medquest/skills/questoes-medicina/SKILL.md)                       | Treine estudantes de Medicina com questões objetivas, casos clínicos, questões discursivas, correção comentada e revisão ativa. Use para graduação, provas médicas e preparação no estilo ENAMED. |

### MedTermo AI

[Documentação do plugin](../plugins/medtermo-ai/README.md) · Versão `0.1.2`

Jogo de adivinhação diagnóstica com cinco tentativas, pistas progressivas e revisão para provas de residência médica.

| Skill                                                                     | Quando usar                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`jogar-medtermo`](../plugins/medtermo-ai/skills/jogar-medtermo/SKILL.md) | Conduza o MedTermo AI, jogo de adivinhação de diagnóstico médico com cinco tentativas e pistas clínicas progressivas. Use quando o usuário pedir uma rodada, um caso para adivinhar, ou continuar um jogo do MedTermo para graduação ou residência. |

### Residência Radar Brasil

[Documentação do plugin](../plugins/residencia-radar-brasil/README.md) · Versão `0.2.0`

Pesquisa e compara vagas, editais, concorrência, notas e chamadas de programas de residência médica no Brasil.

| Skill                                                                                                                 | Quando usar                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`acompanhar-chamadas-residencia`](../plugins/residencia-radar-brasil/skills/acompanhar-chamadas-residencia/SKILL.md) | Use para reconstituir convocações e movimentação de listas de residência.                                                                                                                         |
| [`comparar-ampla-pcd`](../plugins/residencia-radar-brasil/skills/comparar-ampla-pcd/SKILL.md)                         | Use para comparar vagas e notas de ampla concorrência e PcD em residência médica.                                                                                                                 |
| [`comparar-vagas-residencia`](../plugins/residencia-radar-brasil/skills/comparar-vagas-residencia/SKILL.md)           | Use para listar e comparar vagas de residência por especialidade, instituição, estado e edição.                                                                                                   |
| [`organizar-notas-residencia`](../plugins/residencia-radar-brasil/skills/organizar-notas-residencia/SKILL.md)         | Use para ordenar notas e construir panorama de resultados de residência.                                                                                                                          |
| [`residencia-radar`](../plugins/residencia-radar-brasil/skills/residencia-radar/SKILL.md)                             | Pesquisa e compara editais, vagas, concorrência, notas e convocações de residência médica por especialidade, instituição, estado e edição, incluindo reservas PcD quando publicadas oficialmente. |

## estudos

**Estudos e aprendizagem**

### Cognitus

[Documentação do plugin](../plugins/cognitus/README.md) · Versão `0.1.2`

Mentor de aprendizagem ativa que desenvolve raciocínio, retenção e autonomia com método socrático, Feynman, prática deliberada e repetição espaçada.

| Skill                                                                          | Quando usar                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`aprendizagem-ativa`](../plugins/cognitus/skills/aprendizagem-ativa/SKILL.md) | Conduza sessões de estudo como o Cognitus usando diagnóstico, método socrático, técnica de Feynman, prática deliberada, diagramas Mermaid e flashcards Anki. Use quando o estudante quiser aprender, revisar, praticar, preparar-se para uma prova ou desenvolver domínio de um tema. |

### Mentor de Estudos

[Documentação do plugin](../plugins/mentor-de-estudos/README.md) · Versão `0.1.2`

Tutor pessoal para planejar estudos, explicar conteúdos, praticar, revisar e acompanhar o progresso do estudante.

| Skill                                                                                   | Quando usar                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`tutoria-de-estudos`](../plugins/mentor-de-estudos/skills/tutoria-de-estudos/SKILL.md) | Atua como tutor pessoal para aprender, revisar e praticar qualquer assunto. Use quando o estudante pedir explicações, planos de estudo, exercícios, simulados, resumos, mapas mentais, flashcards, revisão ou acompanhamento de progresso. |

### ProvaLab

[Documentação do plugin](../plugins/provalab/README.md) · Versão `0.1.0`

Cria avaliações e cadernos de questões a partir de apostilas, slides, guias e materiais enviados pelo usuário.

| Skill                                                                      | Quando usar                                                                                                                                        |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`criar-avaliacoes`](../plugins/provalab/skills/criar-avaliacoes/SKILL.md) | Cria provas, simulados, estudos dirigidos e cadernos de questões com base em apostilas, slides, guias, anotações e arquivos enviados pelo usuário. |

### Anki Builder

[Documentação do plugin](../plugins/anki-builder/README.md) · Versão `0.1.0`

Criar flashcards básicos, cloze e exportação TSV com origem rastreável.

| Skill                                                                              | Quando usar                                                                   |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [`criar-cloze`](../plugins/anki-builder/skills/criar-cloze/SKILL.md)               | Use para criar cartões Anki com lacunas no formato {{c1::texto}}.             |
| [`criar-flashcards`](../plugins/anki-builder/skills/criar-flashcards/SKILL.md)     | Use para transformar material fornecido em cartões de pergunta e resposta.    |
| [`exportar-anki-tsv`](../plugins/anki-builder/skills/exportar-anki-tsv/SKILL.md)   | Use para exportar cartões básicos ou cloze em TSV UTF-8 importável pelo Anki. |
| [`revisar-flashcards`](../plugins/anki-builder/skills/revisar-flashcards/SKILL.md) | Use para melhorar flashcards ambíguos, longos ou duplicados.                  |

## dados

**Dados e programação**

### DataLab — Análise de Dados

[Documentação do plugin](../plugins/datalab/README.md) · Versão `0.1.0`

Limpar bases, explorar dados, construir gráficos e produzir relatórios reproduzíveis.

| Skill                                                                               | Quando usar                                                                                          |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| [`criar-graficos-dados`](../plugins/datalab/skills/criar-graficos-dados/SKILL.md)   | Use para visualizar tendências, categorias, composição ou distribuição de dados fornecidos.          |
| [`explorar-dados`](../plugins/datalab/skills/explorar-dados/SKILL.md)               | Use para análise exploratória de uma base, distribuições, padrões, correlações e qualidade de dados. |
| [`limpar-base-dados`](../plugins/datalab/skills/limpar-base-dados/SKILL.md)         | Use para limpar CSV, TSV ou Excel, padronizar colunas e avaliar valores ausentes ou duplicados.      |
| [`relatar-analise-dados`](../plugins/datalab/skills/relatar-analise-dados/SKILL.md) | Use para consolidar uma análise em relatório com metodologia, resultados e limitações.               |

### SQL Mentor

[Documentação do plugin](../plugins/sql-mentor/README.md) · Versão `0.1.0`

Ensinar, escrever, depurar e praticar SQL com exemplos controlados.

| Skill                                                                                    | Quando usar                                                                                         |
| ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [`depurar-sql`](../plugins/sql-mentor/skills/depurar-sql/SKILL.md)                       | Use para corrigir erro de sintaxe, resultado inesperado ou consulta lenta.                          |
| [`escrever-consultas-sql`](../plugins/sql-mentor/skills/escrever-consultas-sql/SKILL.md) | Use quando precisar criar SELECTs, agregações, filtros, CTEs ou consultas a partir de uma pergunta. |
| [`explicar-joins-sql`](../plugins/sql-mentor/skills/explicar-joins-sql/SKILL.md)         | Use para ensinar INNER, LEFT, RIGHT e FULL JOIN, cardinalidade e duplicação de linhas.              |
| [`praticar-sql`](../plugins/sql-mentor/skills/praticar-sql/SKILL.md)                     | Use para gerar exercícios SQL graduais com banco fictício e gabarito separado.                      |

### Python Lab

[Documentação do plugin](../plugins/python-lab/README.md) · Versão `0.1.0`

Explicar código, depurar erros, criar exercícios e organizar projetos Python.

| Skill                                                                                        | Quando usar                                                                                           |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [`depurar-python`](../plugins/python-lab/skills/depurar-python/SKILL.md)                     | Use para corrigir traceback, falha de comportamento ou erro em programa Python.                       |
| [`explicar-codigo-python`](../plugins/python-lab/skills/explicar-codigo-python/SKILL.md)     | Use para explicar um trecho Python, fluxo de execução ou comportamento de uma função.                 |
| [`organizar-projeto-python`](../plugins/python-lab/skills/organizar-projeto-python/SKILL.md) | Use para estruturar um projeto Python pequeno, organizar módulos e dependências ou preparar execução. |
| [`praticar-python`](../plugins/python-lab/skills/praticar-python/SKILL.md)                   | Use para criar exercícios e corrigir soluções Python por nível e tema.                                |

### Dashboard Studio

[Documentação do plugin](../plugins/dashboard-studio/README.md) · Versão `0.1.0`

Definir indicadores, modelagem, layout e medidas DAX para dashboards.

| Skill                                                                                                | Quando usar                                                                             |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [`definir-indicadores`](../plugins/dashboard-studio/skills/definir-indicadores/SKILL.md)             | Use para definir KPIs e contratos de métricas de um dashboard.                          |
| [`escrever-dax`](../plugins/dashboard-studio/skills/escrever-dax/SKILL.md)                           | Use para criar ou corrigir medidas DAX no Power BI.                                     |
| [`modelar-dashboard`](../plugins/dashboard-studio/skills/modelar-dashboard/SKILL.md)                 | Use para desenhar modelo estrela, relações, calendário e granularidade de um dashboard. |
| [`planejar-layout-dashboard`](../plugins/dashboard-studio/skills/planejar-layout-dashboard/SKILL.md) | Use para organizar páginas, filtros, gráficos e navegação de um painel.                 |

### terminal-ops

[Documentação do plugin](../plugins/terminal-ops/README.md) · Versão `1.0.0`

Conjunto de skills de extrema autonomia para automação de tarefas no terminal, DevOps, resolução de conflitos e manutenção contínua.

| Skill                                                                                    | Quando usar                                                                                                                                               |
| ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`auto-migrator`](../plugins/terminal-ops/skills/auto-migrator/SKILL.md)                 | Migra automaticamente bases de código legadas para novas versões de frameworks usando varredura via terminal (grep, sed, replace).                        |
| [`auto-onboarder`](../plugins/terminal-ops/skills/auto-onboarder/SKILL.md)               | Configura automaticamente projetos recém-clonados do zero. Instala dependências, cria variáveis de ambiente e sobe bancos de dados via terminal.          |
| [`auto-troubleshooter`](../plugins/terminal-ops/skills/auto-troubleshooter/SKILL.md)     | Agente autônomo de resolução de erros. Roda um comando que está falhando, analisa o stack trace, edita o código e repete até o terminal retornar sucesso. |
| [`git-conflict-resolver`](../plugins/terminal-ops/skills/git-conflict-resolver/SKILL.md) | Lê arquivos em conflito no Git, compreende as intenções de ambas as branches e realiza o merge do código automaticamente pelo terminal.                   |
| [`log-watchdog`](../plugins/terminal-ops/skills/log-watchdog/SKILL.md)                   | Agente em background que vigia logs de um servidor ativo. Quando detecta Exceptions, ele analisa, sugere ou corrige o erro em tempo real.                 |

## pesquisa

**Pesquisa e saúde pública**

### Pesquisa Científica

[Documentação do plugin](../plugins/pesquisa-cientifica/README.md) · Versão `0.1.0`

Buscar literatura, extrair evidências, comparar estudos e organizar referências.

| Skill                                                                                           | Quando usar                                                                              |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [`buscar-literatura`](../plugins/pesquisa-cientifica/skills/buscar-literatura/SKILL.md)         | Use para pesquisar artigos e planejar uma revisão de literatura com fontes verificáveis. |
| [`comparar-estudos`](../plugins/pesquisa-cientifica/skills/comparar-estudos/SKILL.md)           | Use para comparar artigos e explicar convergências, divergências e comparabilidade.      |
| [`extrair-evidencias`](../plugins/pesquisa-cientifica/skills/extrair-evidencias/SKILL.md)       | Use para extrair população, métodos, resultados e limitações de um artigo fornecido.     |
| [`organizar-referencias`](../plugins/pesquisa-cientifica/skills/organizar-referencias/SKILL.md) | Use para conferir DOI, deduplicar e formatar referências bibliográficas.                 |

### Artigo Crítico

[Documentação do plugin](../plugins/artigo-critico/README.md) · Versão `0.1.0`

Avaliar desenho, vieses, estatísticas e aplicabilidade de pesquisas.

| Skill                                                                                                        | Quando usar                                                                                       |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| [`avaliar-aplicabilidade`](../plugins/artigo-critico/skills/avaliar-aplicabilidade/SKILL.md)                 | Use para discutir se resultados de pesquisa se aplicam a uma população ou cenário.                |
| [`avaliar-vieses`](../plugins/artigo-critico/skills/avaliar-vieses/SKILL.md)                                 | Use para analisar riscos de viés de um estudo por domínio metodológico.                           |
| [`identificar-desenho-estudo`](../plugins/artigo-critico/skills/identificar-desenho-estudo/SKILL.md)         | Use para classificar desenho de pesquisa e explicar o que ele permite concluir.                   |
| [`interpretar-estatistica-artigo`](../plugins/artigo-critico/skills/interpretar-estatistica-artigo/SKILL.md) | Use para explicar efeito, precisão, significância e relevância prática em resultados científicos. |

### Dados de Saúde Brasil

[Documentação do plugin](../plugins/dados-saude-brasil/README.md) · Versão `0.2.1`

Consulta simples a dados públicos de doenças no Brasil usando fontes oficiais do SUS.

| Skill                                                                                                    | Quando usar                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`comparar-municipios-saude`](../plugins/dados-saude-brasil/skills/comparar-municipios-saude/SKILL.md)   | Use para comparar dados de doença entre municípios com período e definição equivalentes.                                                                                                                             |
| [`consulta-dados-doencas`](../plugins/dados-saude-brasil/skills/consulta-dados-doencas/SKILL.md)         | Pesquisa notificações, casos, internações e óbitos por doença em município, estado ou Brasil usando fontes públicas oficiais. Use quando o usuário pedir dados, estatísticas ou uma consulta epidemiológica simples. |
| [`explicar-indicadores-saude`](../plugins/dados-saude-brasil/skills/explicar-indicadores-saude/SKILL.md) | Use para distinguir notificações, casos, internações, óbitos, incidência, mortalidade e letalidade.                                                                                                                  |
| [`serie-historica-saude`](../plugins/dados-saude-brasil/skills/serie-historica-saude/SKILL.md)           | Use para organizar tendência anual ou mensal de casos, internações ou óbitos.                                                                                                                                        |

## criacao

**Design, documentos e conteúdo**

### PostLab — Designer Criativo

[Documentação do plugin](../plugins/postlab/README.md) · Versão `0.2.1`

Designer de posts criativos com artes, fotos, legendas e carrosséis para redes sociais.

| Skill                                                                                     | Quando usar                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`adaptar-formato-post`](../plugins/postlab/skills/adaptar-formato-post/SKILL.md)         | Use para adaptar arte ou conteúdo entre formatos e redes sociais.                                                                                                                                                                                                  |
| [`criar-posts-criativos`](../plugins/postlab/skills/criar-posts-criativos/SKILL.md)       | Criar e refinar posts bonitos e criativos para Instagram, LinkedIn e outras redes, com direção de arte, imagens, legendas e carrosséis. Usar para design de post, arte para rede social, melhoria visual, campanha visual ou carrossel com identidade consistente. |
| [`manter-identidade-visual`](../plugins/postlab/skills/manter-identidade-visual/SKILL.md) | Use para criar guia visual ou aplicar consistência a uma série de posts.                                                                                                                                                                                           |
| [`planejar-carrossel`](../plugins/postlab/skills/planejar-carrossel/SKILL.md)             | Use para roteirizar páginas de carrossel educativo ou profissional.                                                                                                                                                                                                |
| [`revisar-texto-arte`](../plugins/postlab/skills/revisar-texto-arte/SKILL.md)             | Use para identificar erros de ortografia, conteúdo e legibilidade em imagem de post.                                                                                                                                                                               |

### LinkedIn Conteúdo Diário

[Documentação do plugin](../plugins/linkedin-conteudo-diario/README.md) · Versão `0.1.1`

Cria, valida e agenda lotes diários de posts educativos com imagens para LinkedIn.

| Skill                                                                                                      | Quando usar                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`linkedin-conteudo-diario`](../plugins/linkedin-conteudo-diario/skills/linkedin-conteudo-diario/SKILL.md) | Cria e agenda lotes diários de posts educativos para LinkedIn sobre dados, Python, IA, machine learning, SQL, Excel e temas relacionados. Use quando o usuário pedir posts para LinkedIn, um lote diário, conteúdo com imagens ou publicação distribuída durante o dia. O padrão é cinco posts com imagens, horários de Brasília e uma aprovação explícita do lote antes do agendamento. |

### Resumo Visual Manuscrito

[Documentação do plugin](../plugins/resumo-visual-manuscrito/README.md) · Versão `0.1.2`

Transforma qualquer tema ou material de estudo em um resumo visual manuscrito, didático, organizado e focado em revisão de prova.

| Skill                                                                                            | Quando usar                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`criar-resumo-visual`](../plugins/resumo-visual-manuscrito/skills/criar-resumo-visual/SKILL.md) | Crie um resumo visual manuscrito premium sobre qualquer tema ou material fornecido, para compreensão rápida, revisão e memorização. Use quando o usuário pedir resumo visual, folha de estudos manuscrita, anotação de caderno, mapa visual de revisão ou material visual para prova. |

### VisualExplain

[Documentação do plugin](../plugins/visualexplain/README.md) · Versão `0.2.1`

Esqueleto para transformar materiais em explicações visuais animadas com roteiro e HTML.

| Skill                                                                                                 | Quando usar                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`animar-processo-explicativo`](../plugins/visualexplain/skills/animar-processo-explicativo/SKILL.md) | Use para transformar um processo descrito em etapas visuais animadas em HTML.                                                                                                                                        |
| [`criar-linha-tempo-visual`](../plugins/visualexplain/skills/criar-linha-tempo-visual/SKILL.md)       | Use para explicar eventos históricos ou etapas temporais de um material.                                                                                                                                             |
| [`explicar-visual-animado`](../plugins/visualexplain/skills/explicar-visual-animado/SKILL.md)         | Transformar artigos, PDFs, slides, documentos e texto em explicações visuais animadas em HTML. Usar quando o usuário pedir aula visual, slide animado, explicação interativa ou transformação visual de um material. |
| [`incluir-quiz-visual`](../plugins/visualexplain/skills/incluir-quiz-visual/SKILL.md)                 | Use para adicionar perguntas objetivas e feedback em uma explicação HTML.                                                                                                                                            |

### Documento Studio

[Documentação do plugin](../plugins/documento-studio/README.md) · Versão `0.1.0`

Criar relatórios, formatar documentos, preparar apresentações e revisar PDFs.

| Skill                                                                                                | Quando usar                                                                        |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [`criar-relatorio-documento`](../plugins/documento-studio/skills/criar-relatorio-documento/SKILL.md) | Use para estruturar e produzir relatório a partir de fatos e materiais fornecidos. |
| [`formatar-documento`](../plugins/documento-studio/skills/formatar-documento/SKILL.md)               | Use para aplicar estilos, hierarquia, sumário, tabelas e paginação a um documento. |
| [`montar-apresentacao`](../plugins/documento-studio/skills/montar-apresentacao/SKILL.md)             | Use para transformar material em roteiro ou arquivo de slides organizado.          |
| [`revisar-pdf`](../plugins/documento-studio/skills/revisar-pdf/SKILL.md)                             | Use para verificar conteúdo, legibilidade, paginação e problemas visuais em PDF.   |

### LinkedIn Design Kit

[Documentação do plugin](../plugins/linkedin-post-design-kit/README.md) · Versão `0.1.1`

Cria conceitos, textos e direções visuais para posts e carrosséis profissionais no LinkedIn, usando repositórios abertos de design como referência.

| Skill                                                                                                  | Quando usar                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`linkedin-post-designer`](../plugins/linkedin-post-design-kit/skills/linkedin-post-designer/SKILL.md) | Cria e refina conteúdo e peças visuais para LinkedIn, como artes únicas, carrosséis e infográficos. Use quando o usuário pedir um post pronto, uma legenda, um roteiro visual ou orientação para montar uma peça profissional para LinkedIn. |

### LinkedIn Design Studio

[Documentação do plugin](../plugins/linkedin-design-studio/README.md) · Versão `0.1.1`

A design assistant for LinkedIn posts, carousels and explainers, with workflows inspired by Penpot, Excalidraw and tldraw.

| Skill                                                                                                                  | Quando usar                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`excalidraw-linkedin-infographic`](../plugins/linkedin-design-studio/skills/excalidraw-linkedin-infographic/SKILL.md) | Transforma conceitos, processos e comparações em infográficos e carrosséis didáticos com traços desenhados à mão. Use quando setas, caixas, ícones simples ou fluxos ajudarem a explicar uma ideia.              |
| [`linkedin-design-router`](../plugins/linkedin-design-studio/skills/linkedin-design-router/SKILL.md)                   | Escolhe um fluxo visual para criar posts, carrosséis, infográficos e explicações para LinkedIn. Use quando o pedido não indicar qual abordagem visual adotar ou quando o usuário quiser combinar estilos.        |
| [`penpot-linkedin-design`](../plugins/linkedin-design-studio/skills/penpot-linkedin-design/SKILL.md)                   | Planeja posts estáticos e carrosséis de LinkedIn com aparência profissional, componentes reutilizáveis e identidade visual consistente. Use para peças de marca, educação, anúncios, dicas, dados ou divulgação. |
| [`tldraw-linkedin-canvas`](../plugins/linkedin-design-studio/skills/tldraw-linkedin-canvas/SKILL.md)                   | Organiza ideias e narrativas de LinkedIn em uma tela ampla com blocos, setas, anotações e storyboard. Use para brainstorm, mapas de conteúdo, fluxos e planejamento visual antes da arte final.                  |

## carreira

**Carreira e concursos**

### Carreira Lab

[Documentação do plugin](../plugins/carreira-lab/README.md) · Versão `0.1.0`

Adaptar currículo, revisar perfil, praticar entrevista e mapear evidências de competências.

| Skill                                                                                          | Quando usar                                                                                |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [`adaptar-curriculo`](../plugins/carreira-lab/skills/adaptar-curriculo/SKILL.md)               | Use para adaptar currículo ao anúncio sem inventar qualificações.                          |
| [`mapear-competencias-vaga`](../plugins/carreira-lab/skills/mapear-competencias-vaga/SKILL.md) | Use para comparar perfil e requisitos e planejar portfólio ou preparação.                  |
| [`revisar-perfil-linkedin`](../plugins/carreira-lab/skills/revisar-perfil-linkedin/SKILL.md)   | Use para redigir título, Sobre e experiências de LinkedIn com base no histórico informado. |
| [`simular-entrevista`](../plugins/carreira-lab/skills/simular-entrevista/SKILL.md)             | Use para praticar entrevista de emprego técnica ou comportamental com feedback.            |

### Edital Fácil

[Documentação do plugin](../plugins/edital-facil/README.md) · Versão `0.2.0`

Lê editais de concursos e seleções e transforma requisitos, etapas, salários e prazos em um resumo e checklist prático.

| Skill                                                                                            | Quando usar                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`comparar-editais`](../plugins/edital-facil/skills/comparar-editais/SKILL.md)                   | Use para comparar seleções ou versões de um edital e identificar mudanças.                                                                                                                  |
| [`extrair-requisitos-edital`](../plugins/edital-facil/skills/extrair-requisitos-edital/SKILL.md) | Use para organizar escolaridade, experiência, documentos, cotas e condições de um edital.                                                                                                   |
| [`ler-editais`](../plugins/edital-facil/skills/ler-editais/SKILL.md)                             | Analisa editais de concursos, seleções e residências para localizar cargos, requisitos, salários, etapas, cotas, documentos, prazos e regras de inscrição com referência ao texto original. |
| [`montar-checklist-edital`](../plugins/edital-facil/skills/montar-checklist-edital/SKILL.md)     | Use para criar lista de documentos e ações de inscrição ou matrícula a partir de edital.                                                                                                    |
| [`organizar-prazos-edital`](../plugins/edital-facil/skills/organizar-prazos-edital/SKILL.md)     | Use para montar cronograma de inscrição, recursos, provas e resultados de um edital.                                                                                                        |

## desenvolvimento

**Plugins, GitHub e APIs**

### GitHub Organizer

[Documentação do plugin](../plugins/github-organizer/README.md) · Versão `0.1.0`

Melhorar README, gerar catálogo, registrar mudanças e conferir links.

| Skill                                                                                                    | Quando usar                                                                                                                                                               |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`catalogar-plugins`](../plugins/github-organizer/skills/catalogar-plugins/SKILL.md)                     | Use para gerar índice de plugins e skills a partir dos arquivos reais de um repositório.                                                                                  |
| [`escrever-changelog`](../plugins/github-organizer/skills/escrever-changelog/SKILL.md)                   | Use para documentar mudanças entre versões ou commits.                                                                                                                    |
| [`melhorar-readme`](../plugins/github-organizer/skills/melhorar-readme/SKILL.md)                         | Use para criar ou atualizar README de projeto com instruções verificáveis.                                                                                                |
| [`repo-beautifier`](../plugins/github-organizer/skills/repo-beautifier/SKILL.md)                         | Organiza a estrutura de pastas do repositório, adiciona arquivos de comunidade, badges, CI/CD, e ferramentas de qualidade para deixar o projeto com padrão internacional. |
| [`verificar-links-repositorio`](../plugins/github-organizer/skills/verificar-links-repositorio/SKILL.md) | Use para encontrar links quebrados ou caminhos inexistentes na documentação.                                                                                              |

### Skill Auditor

[Documentação do plugin](../plugins/skill-auditor/README.md) · Versão `0.1.0`

Avaliar estrutura, instruções, recursos e comportamento de skills com casos de uso.

| Skill                                                                                         | Quando usar                                                                                    |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [`auditar-skill`](../plugins/skill-auditor/skills/auditar-skill/SKILL.md)                     | Use para revisar SKILL.md quanto a escopo, clareza, recursos e promessas.                      |
| [`avaliar-exemplos-skill`](../plugins/skill-auditor/skills/avaliar-exemplos-skill/SKILL.md)   | Use para criar e executar casos que verifiquem comportamento real de uma skill.                |
| [`revisar-limites-skill`](../plugins/skill-auditor/skills/revisar-limites-skill/SKILL.md)     | Use para verificar tratamento de fontes, autorização, privacidade e dependências em workflows. |
| [`validar-estrutura-skill`](../plugins/skill-auditor/skills/validar-estrutura-skill/SKILL.md) | Use para verificar YAML, nome, referências e arquivos de uma skill.                            |

### Plugin Builder

[Documentação do plugin](../plugins/plugin-builder/README.md) · Versão `0.1.0`

Estruturar plugins de skills, preparar manifestos, documentar requisitos e empacotar versões.

| Skill                                                                                              | Quando usar                                                                       |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [`documentar-plugin`](../plugins/plugin-builder/skills/documentar-plugin/SKILL.md)                 | Use para escrever instruções de uso, configuração e limitações de um pacote.      |
| [`empacotar-plugin`](../plugins/plugin-builder/skills/empacotar-plugin/SKILL.md)                   | Use para preparar arquivo ZIP ou tar.gz de plugin quando solicitado.              |
| [`estruturar-plugin`](../plugins/plugin-builder/skills/estruturar-plugin/SKILL.md)                 | Use para organizar um plugin de skills ou integrar arquivos existentes em pacote. |
| [`preparar-manifesto-plugin`](../plugins/plugin-builder/skills/preparar-manifesto-plugin/SKILL.md) | Use para criar ou revisar plugin.json e overlays de compatibilidade.              |

### API Explorer

[Documentação do plugin](../plugins/api-explorer/README.md) · Versão `0.1.0`

Ler documentação, realizar consultas autorizadas, paginar resultados e documentar respostas.

| Skill                                                                                        | Quando usar                                                                                   |
| -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [`documentar-resposta-api`](../plugins/api-explorer/skills/documentar-resposta-api/SKILL.md) | Use para produzir dicionário de campos e contrato a partir de documentação e respostas reais. |
| [`ler-documentacao-api`](../plugins/api-explorer/skills/ler-documentacao-api/SKILL.md)       | Use para entender endpoints, autenticação, filtros e limites de uma API.                      |
| [`paginar-api`](../plugins/api-explorer/skills/paginar-api/SKILL.md)                         | Use para coletar várias páginas de resultados de uma API com controle de limites.             |
| [`testar-consulta-api`](../plugins/api-explorer/skills/testar-consulta-api/SKILL.md)         | Use para testar consulta HTTP de leitura a endpoint documentado.                              |

### asclepio

[Documentação do plugin](../plugins/asclepio/README.md) · Versão `1.0.0`

Ativa o modo autônomo extremo. O agente deve assumir controle total, resolver problemas por conta própria, evitar perguntas e rodar até terminar a tarefa.

| Skill                                                      | Quando usar                                                                                                                                                                              |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`asclepio`](../plugins/asclepio/skills/asclepio/SKILL.md) | Ativa o modo autônomo extremo com regras avançadas de resiliência, logging, delegação e qualidade. O agente deve assumir controle total, evitar perguntas e rodar até terminar a tarefa. |

### agentes-autonomos

[Documentação do plugin](../plugins/agentes-autonomos/README.md) · Versão `1.0.0`

Uma suíte de agentes trabalhadores autônomos que orquestram tarefas complexas no terminal: Triagem, Segurança, Documentação, Dados e Migração.

| Skill                                                                                 | Quando usar                                                                                                                                               |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`data-miner`](../plugins/agentes-autonomos/skills/data-miner/SKILL.md)               | Agente de engenharia de dados (ETL). Extrai dados brutos de APIs, limpa com Python, gera bancos de dados e relatórios de métricas.                        |
| [`docbot-architect`](../plugins/agentes-autonomos/skills/docbot-architect/SKILL.md)   | Agente de engenharia reversa. Varre o código, deduz a arquitetura e gera diagramas (Mermaid) e documentação (JSDoc/Docstring) massivamente.               |
| [`legacy-modernizer`](../plugins/agentes-autonomos/skills/legacy-modernizer/SKILL.md) | Agente de migração. Pega um projeto legado (versões antigas) e atualiza para linguagens e frameworks modernos de forma iterativa.                         |
| [`secops-auditor`](../plugins/agentes-autonomos/skills/secops-auditor/SKILL.md)       | Engenheiro de segurança cibernética autônomo. Roda scanners no terminal, descobre bibliotecas vulneráveis e tenta consertar ou atualizar automaticamente. |
| [`triage-maintainer`](../plugins/agentes-autonomos/skills/triage-maintainer/SKILL.md) | Atua como mantenedor Open Source. Lê issues do GitHub, tenta reproduzir o erro isoladamente, escreve a correção, testa e abre PRs automaticamente.        |

## financas

**Finanças e comparações**

### InvestIA — Análise de Investimentos

[Documentação do plugin](../plugins/investia/README.md) · Versão `0.2.1`

Pesquisa e compara investimentos com fundamentos, notícias, cenários e simulação de risco usando ferramentas disponíveis no ChatGPT.

| Skill                                                                                                | Quando usar                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`analisar-investimentos-ia`](../plugins/investia/skills/analisar-investimentos-ia/SKILL.md)         | Analisar ações, ETFs, FIIs e criptoativos com fundamentos, demonstrações, notícias, análise técnica e gestão de risco. Usar para pesquisar um ativo, comparar investimentos, avaliar uma carteira ou simular tamanho de posição com IA. |
| [`comparar-ativos`](../plugins/investia/skills/comparar-ativos/SKILL.md)                             | Use para comparar ações, ETFs, FIIs ou outros ativos por critérios equivalentes.                                                                                                                                                        |
| [`ler-demonstracoes-financeiras`](../plugins/investia/skills/ler-demonstracoes-financeiras/SKILL.md) | Use para analisar DRE, balanço e fluxo de caixa de uma empresa.                                                                                                                                                                         |
| [`simular-cenarios-investimento`](../plugins/investia/skills/simular-cenarios-investimento/SKILL.md) | Use para projetar cenários com aportes, retorno, inflação e custos declarados.                                                                                                                                                          |

### Comparador de carros

[Documentação do plugin](../plugins/comparador-precos-carros/README.md) · Versão `0.2.1`

Pesquisa e compara preços de carros no Brasil por categoria, marca, modelo, versão e região, com fontes e critérios claros.

| Skill                                                                                                    | Quando usar                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`checklist-avaliar-carro`](../plugins/comparador-precos-carros/skills/checklist-avaliar-carro/SKILL.md) | Use para orientar inspeção documental e visual antes de compra de usado.                                                                                                                                                                                                         |
| [`comparar-precos-carros`](../plugins/comparador-precos-carros/skills/comparar-precos-carros/SKILL.md)   | Pesquisa e compara preços de carros no Brasil por categoria, marca, modelo, versão, ano e região. Use quando a pessoa quiser encontrar veículos dentro de um orçamento, comparar carros novos ou usados, consultar preço de mercado ou FIPE, ou avaliar consumo e custos de uso. |
| [`comparar-versoes-carro`](../plugins/comparador-precos-carros/skills/comparar-versoes-carro/SKILL.md)   | Use para comparar equipamentos, motorização, segurança e preço por versão/ano.                                                                                                                                                                                                   |
| [`estimar-custo-carro`](../plugins/comparador-precos-carros/skills/estimar-custo-carro/SKILL.md)         | Use para estimar gasto mensal e anual de veículo com parâmetros locais.                                                                                                                                                                                                          |

### TokenMeter Universal

[Documentação do plugin](../plugins/tokenmeter-universal/README.md) · Versão `1.0.1`

Registro portátil de consumo de tokens com relatórios diários, semanais, mensais, anuais e total acumulado. Importação de metadados, custos configuráveis e MCP local.

| Skill                                                                          | Quando usar                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`medir-tokens`](../plugins/tokenmeter-universal/skills/medir-tokens/SKILL.md) | Medir e registrar tokens de IA por dia, semana, mês, ano e total acumulado. Usar para auditoria de consumo, importação CSV/JSON/JSONL, metadados OpenAI/compatíveis, Claude, Gemini e Ollama, custos configuráveis e estimativas de texto. |
