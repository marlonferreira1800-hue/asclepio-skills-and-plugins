<!-- Gerado por scripts/generate_catalog.py. Editar manifestos, skills ou metadata/catalog.json. -->

# Catálogo de plugins e skills

39 plugins e 150 skills. Os nomes abaixo são os identificadores reais dos arquivos. Para exemplos e dependências, abra o README de cada plugin.

[Voltar ao início](../README.md) · [Guia rápido](guia-rapido.md)

## medicina

**Medicina e residência**

### MedQuest — Medicina por Questões

[Documentação do plugin](../plugins/medquest/README.md) · Versão `0.2.0`

Treino ativo de Medicina por questões, casos clínicos e correção comentada.

| Skill | Quando usar |
|---|---|
| [`analisar-erros-estudo`](../plugins/medquest/skills/analisar-erros-estudo/SKILL.md) | Use para interpretar respostas de simulados e orientar revisão específica. |
| [`classificar-questoes-medicas`](../plugins/medquest/skills/classificar-questoes-medicas/SKILL.md) | Use para organizar questões por tema, habilidade e nível cognitivo. |
| [`criar-prova-equivalente`](../plugins/medquest/skills/criar-prova-equivalente/SKILL.md) | Use para gerar nova versão de prova preservando objetivos e distribuição. |
| [`questoes-medicina`](../plugins/medquest/skills/questoes-medicina/SKILL.md) | Treine estudantes de Medicina com questões objetivas, casos clínicos, questões discursivas, correção comentada e revisão ativa. Use para graduação, provas médicas e preparação no estilo ENAMED. |

### MedTermo AI

[Documentação do plugin](../plugins/medtermo-ai/README.md) · Versão `0.1.1`

Jogo de adivinhação diagnóstica com cinco tentativas, pistas progressivas e revisão para provas de residência médica.

| Skill | Quando usar |
|---|---|
| [`jogar-medtermo`](../plugins/medtermo-ai/skills/jogar-medtermo/SKILL.md) | Conduza o MedTermo AI, jogo de adivinhação de diagnóstico médico com cinco tentativas e pistas clínicas progressivas. Use quando o usuário pedir uma rodada, um caso para adivinhar, ou continuar um jogo do MedTermo para graduação ou residência. |

### Residência Radar Brasil

[Documentação do plugin](../plugins/residencia-radar-brasil/README.md) · Versão `0.2.0`

Pesquisa e compara vagas, editais, concorrência, notas e chamadas de programas de residência médica no Brasil.

| Skill | Quando usar |
|---|---|
| [`acompanhar-chamadas-residencia`](../plugins/residencia-radar-brasil/skills/acompanhar-chamadas-residencia/SKILL.md) | Use para reconstituir convocações e movimentação de listas de residência. |
| [`comparar-ampla-pcd`](../plugins/residencia-radar-brasil/skills/comparar-ampla-pcd/SKILL.md) | Use para comparar vagas e notas de ampla concorrência e PcD em residência médica. |
| [`comparar-vagas-residencia`](../plugins/residencia-radar-brasil/skills/comparar-vagas-residencia/SKILL.md) | Use para listar e comparar vagas de residência por especialidade, instituição, estado e edição. |
| [`organizar-notas-residencia`](../plugins/residencia-radar-brasil/skills/organizar-notas-residencia/SKILL.md) | Use para ordenar notas e construir panorama de resultados de residência. |
| [`residencia-radar`](../plugins/residencia-radar-brasil/skills/residencia-radar/SKILL.md) | Pesquisa e compara editais, vagas, concorrência, notas e convocações de residência médica por especialidade, instituição, estado e edição, incluindo reservas PcD quando publicadas oficialmente. |

## estudos

**Estudos e aprendizagem**

### Cognitus

[Documentação do plugin](../plugins/cognitus/README.md) · Versão `0.1.1`

Mentor de aprendizagem ativa que desenvolve raciocínio, retenção e autonomia com método socrático, Feynman, prática deliberada e repetição espaçada.

| Skill | Quando usar |
|---|---|
| [`aprendizagem-ativa`](../plugins/cognitus/skills/aprendizagem-ativa/SKILL.md) | Conduza sessões de estudo como o Cognitus usando diagnóstico, método socrático, técnica de Feynman, prática deliberada, diagramas Mermaid e flashcards Anki. Use quando o estudante quiser aprender, revisar, praticar, preparar-se para uma prova ou desenvolver domínio de um tema. |

### Mentor de Estudos

[Documentação do plugin](../plugins/mentor-de-estudos/README.md) · Versão `0.1.1`

Tutor pessoal para planejar estudos, explicar conteúdos, praticar, revisar e acompanhar o progresso do estudante.

| Skill | Quando usar |
|---|---|
| [`tutoria-de-estudos`](../plugins/mentor-de-estudos/skills/tutoria-de-estudos/SKILL.md) | Atua como tutor pessoal para aprender, revisar e praticar qualquer assunto. Use quando o estudante pedir explicações, planos de estudo, exercícios, simulados, resumos, mapas mentais, flashcards, revisão ou acompanhamento de progresso. |

### ProvaLab

[Documentação do plugin](../plugins/provalab/README.md) · Versão `0.1.0`

Cria avaliações e cadernos de questões a partir de apostilas, slides, guias e materiais enviados pelo usuário.

| Skill | Quando usar |
|---|---|
| [`criar-avaliacoes`](../plugins/provalab/skills/criar-avaliacoes/SKILL.md) | Cria provas, simulados, estudos dirigidos e cadernos de questões com base em apostilas, slides, guias, anotações e arquivos enviados pelo usuário. |

### Anki Builder

[Documentação do plugin](../plugins/anki-builder/README.md) · Versão `0.1.0`

Criar flashcards básicos, cloze e exportação TSV com origem rastreável.

| Skill | Quando usar |
|---|---|
| [`criar-cloze`](../plugins/anki-builder/skills/criar-cloze/SKILL.md) | Use para criar cartões Anki com lacunas no formato {{c1::texto}}. |
| [`criar-flashcards`](../plugins/anki-builder/skills/criar-flashcards/SKILL.md) | Use para transformar material fornecido em cartões de pergunta e resposta. |
| [`exportar-anki-tsv`](../plugins/anki-builder/skills/exportar-anki-tsv/SKILL.md) | Use para exportar cartões básicos ou cloze em TSV UTF-8 importável pelo Anki. |
| [`revisar-flashcards`](../plugins/anki-builder/skills/revisar-flashcards/SKILL.md) | Use para melhorar flashcards ambíguos, longos ou duplicados. |

## dados

**Dados e programação**

### DataLab — Análise de Dados

[Documentação do plugin](../plugins/datalab/README.md) · Versão `0.2.0`

Limpar bases, explorar dados, construir gráficos e produzir relatórios reproduzíveis.

| Skill | Quando usar |
|---|---|
| [`criar-figura-publicacao`](../plugins/datalab/skills/criar-figura-publicacao/SKILL.md) | Use para produzir gráfico exato adequado à publicação. |
| [`criar-graficos-dados`](../plugins/datalab/skills/criar-graficos-dados/SKILL.md) | Use para visualizar tendências, categorias, composição ou distribuição de dados fornecidos. |
| [`escrever-legenda-cientifica`](../plugins/datalab/skills/escrever-legenda-cientifica/SKILL.md) | Use para redigir legenda que permita entender uma figura sem depender do corpo do artigo. |
| [`explorar-dados`](../plugins/datalab/skills/explorar-dados/SKILL.md) | Use para análise exploratória de uma base, distribuições, padrões, correlações e qualidade de dados. |
| [`exportar-figura-cientifica`](../plugins/datalab/skills/exportar-figura-cientifica/SKILL.md) | Use para preparar formatos e resolução de figura conforme destino. |
| [`limpar-base-dados`](../plugins/datalab/skills/limpar-base-dados/SKILL.md) | Use para limpar CSV, TSV ou Excel, padronizar colunas e avaliar valores ausentes ou duplicados. |
| [`padronizar-paineis-figura`](../plugins/datalab/skills/padronizar-paineis-figura/SKILL.md) | Use para organizar figuras multipainel com escalas e rótulos consistentes. |
| [`relatar-analise-dados`](../plugins/datalab/skills/relatar-analise-dados/SKILL.md) | Use para consolidar uma análise em relatório com metodologia, resultados e limitações. |

### SQL Mentor

[Documentação do plugin](../plugins/sql-mentor/README.md) · Versão `0.1.0`

Ensinar, escrever, depurar e praticar SQL com exemplos controlados.

| Skill | Quando usar |
|---|---|
| [`depurar-sql`](../plugins/sql-mentor/skills/depurar-sql/SKILL.md) | Use para corrigir erro de sintaxe, resultado inesperado ou consulta lenta. |
| [`escrever-consultas-sql`](../plugins/sql-mentor/skills/escrever-consultas-sql/SKILL.md) | Use quando precisar criar SELECTs, agregações, filtros, CTEs ou consultas a partir de uma pergunta. |
| [`explicar-joins-sql`](../plugins/sql-mentor/skills/explicar-joins-sql/SKILL.md) | Use para ensinar INNER, LEFT, RIGHT e FULL JOIN, cardinalidade e duplicação de linhas. |
| [`praticar-sql`](../plugins/sql-mentor/skills/praticar-sql/SKILL.md) | Use para gerar exercícios SQL graduais com banco fictício e gabarito separado. |

### Python Lab

[Documentação do plugin](../plugins/python-lab/README.md) · Versão `0.1.0`

Explicar código, depurar erros, criar exercícios e organizar projetos Python.

| Skill | Quando usar |
|---|---|
| [`depurar-python`](../plugins/python-lab/skills/depurar-python/SKILL.md) | Use para corrigir traceback, falha de comportamento ou erro em programa Python. |
| [`explicar-codigo-python`](../plugins/python-lab/skills/explicar-codigo-python/SKILL.md) | Use para explicar um trecho Python, fluxo de execução ou comportamento de uma função. |
| [`organizar-projeto-python`](../plugins/python-lab/skills/organizar-projeto-python/SKILL.md) | Use para estruturar um projeto Python pequeno, organizar módulos e dependências ou preparar execução. |
| [`praticar-python`](../plugins/python-lab/skills/praticar-python/SKILL.md) | Use para criar exercícios e corrigir soluções Python por nível e tema. |

### Dashboard Studio

[Documentação do plugin](../plugins/dashboard-studio/README.md) · Versão `0.1.0`

Definir indicadores, modelagem, layout e medidas DAX para dashboards.

| Skill | Quando usar |
|---|---|
| [`definir-indicadores`](../plugins/dashboard-studio/skills/definir-indicadores/SKILL.md) | Use para definir KPIs e contratos de métricas de um dashboard. |
| [`escrever-dax`](../plugins/dashboard-studio/skills/escrever-dax/SKILL.md) | Use para criar ou corrigir medidas DAX no Power BI. |
| [`modelar-dashboard`](../plugins/dashboard-studio/skills/modelar-dashboard/SKILL.md) | Use para desenhar modelo estrela, relações, calendário e granularidade de um dashboard. |
| [`planejar-layout-dashboard`](../plugins/dashboard-studio/skills/planejar-layout-dashboard/SKILL.md) | Use para organizar páginas, filtros, gráficos e navegação de um painel. |

## pesquisa

**Pesquisa e saúde pública**

### Pesquisa Científica

[Documentação do plugin](../plugins/pesquisa-cientifica/README.md) · Versão `0.1.0`

Buscar literatura, extrair evidências, comparar estudos e organizar referências.

| Skill | Quando usar |
|---|---|
| [`buscar-literatura`](../plugins/pesquisa-cientifica/skills/buscar-literatura/SKILL.md) | Use para pesquisar artigos e planejar uma revisão de literatura com fontes verificáveis. |
| [`comparar-estudos`](../plugins/pesquisa-cientifica/skills/comparar-estudos/SKILL.md) | Use para comparar artigos e explicar convergências, divergências e comparabilidade. |
| [`extrair-evidencias`](../plugins/pesquisa-cientifica/skills/extrair-evidencias/SKILL.md) | Use para extrair população, métodos, resultados e limitações de um artigo fornecido. |
| [`organizar-referencias`](../plugins/pesquisa-cientifica/skills/organizar-referencias/SKILL.md) | Use para conferir DOI, deduplicar e formatar referências bibliográficas. |

### Artigo Crítico

[Documentação do plugin](../plugins/artigo-critico/README.md) · Versão `0.1.0`

Avaliar desenho, vieses, estatísticas e aplicabilidade de pesquisas.

| Skill | Quando usar |
|---|---|
| [`avaliar-aplicabilidade`](../plugins/artigo-critico/skills/avaliar-aplicabilidade/SKILL.md) | Use para discutir se resultados de pesquisa se aplicam a uma população ou cenário. |
| [`avaliar-vieses`](../plugins/artigo-critico/skills/avaliar-vieses/SKILL.md) | Use para analisar riscos de viés de um estudo por domínio metodológico. |
| [`identificar-desenho-estudo`](../plugins/artigo-critico/skills/identificar-desenho-estudo/SKILL.md) | Use para classificar desenho de pesquisa e explicar o que ele permite concluir. |
| [`interpretar-estatistica-artigo`](../plugins/artigo-critico/skills/interpretar-estatistica-artigo/SKILL.md) | Use para explicar efeito, precisão, significância e relevância prática em resultados científicos. |

### Dados de Saúde Brasil

[Documentação do plugin](../plugins/dados-saude-brasil/README.md) · Versão `0.2.0`

Consulta simples a dados públicos de doenças no Brasil usando fontes oficiais do SUS.

| Skill | Quando usar |
|---|---|
| [`comparar-municipios-saude`](../plugins/dados-saude-brasil/skills/comparar-municipios-saude/SKILL.md) | Use para comparar dados de doença entre municípios com período e definição equivalentes. |
| [`consulta-dados-doencas`](../plugins/dados-saude-brasil/skills/consulta-dados-doencas/SKILL.md) | Pesquisa notificações, casos, internações e óbitos por doença em município, estado ou Brasil usando fontes públicas oficiais. Use quando o usuário pedir dados, estatísticas ou uma consulta epidemiológica simples. |
| [`explicar-indicadores-saude`](../plugins/dados-saude-brasil/skills/explicar-indicadores-saude/SKILL.md) | Use para distinguir notificações, casos, internações, óbitos, incidência, mortalidade e letalidade. |
| [`serie-historica-saude`](../plugins/dados-saude-brasil/skills/serie-historica-saude/SKILL.md) | Use para organizar tendência anual ou mensal de casos, internações ou óbitos. |

### Projeto Científico

[Documentação do plugin](../plugins/projeto-cientifico/README.md) · Versão `0.1.0`

Formular hipóteses, definir variáveis, planejar amostra e estruturar protocolos de pesquisa.

| Skill | Quando usar |
|---|---|
| [`definir-variaveis-pesquisa`](../plugins/projeto-cientifico/skills/definir-variaveis-pesquisa/SKILL.md) | Use para criar dicionário de variáveis e desfechos. |
| [`estruturar-protocolo-pesquisa`](../plugins/projeto-cientifico/skills/estruturar-protocolo-pesquisa/SKILL.md) | Use para montar protocolo a partir de pergunta e desenho. |
| [`formular-hipotese-pesquisa`](../plugins/projeto-cientifico/skills/formular-hipotese-pesquisa/SKILL.md) | Use para transformar tema em pergunta e hipótese testável. |
| [`planejar-amostra-pesquisa`](../plugins/projeto-cientifico/skills/planejar-amostra-pesquisa/SKILL.md) | Use para definir estratégia amostral e parâmetros de tamanho amostral. |

### Bioestatística Lab

[Documentação do plugin](../plugins/bioestatistica-lab/README.md) · Versão `0.1.0`

Escolher testes, avaliar pressupostos, calcular efeitos e interpretar resultados de pesquisa.

| Skill | Quando usar |
|---|---|
| [`avaliar-pressupostos-estatisticos`](../plugins/bioestatistica-lab/skills/avaliar-pressupostos-estatisticos/SKILL.md) | Use para conferir condições para análise estatística. |
| [`calcular-efeitos-estatisticos`](../plugins/bioestatistica-lab/skills/calcular-efeitos-estatisticos/SKILL.md) | Use para estimar magnitude de efeitos e intervalos de confiança. |
| [`escolher-teste-estatistico`](../plugins/bioestatistica-lab/skills/escolher-teste-estatistico/SKILL.md) | Use para selecionar método conforme pergunta, desenho e variáveis. |
| [`interpretar-resultados-pesquisa`](../plugins/bioestatistica-lab/skills/interpretar-resultados-pesquisa/SKILL.md) | Use para redigir interpretação estatística com relevância prática. |

### Ensaios Clínicos Radar

[Documentação do plugin](../plugins/ensaios-clinicos-radar/README.md) · Versão `0.1.0`

Buscar ensaios registrados, comparar protocolos e organizar fases e status com fontes.

| Skill | Quando usar |
|---|---|
| [`buscar-ensaios-registrados`](../plugins/ensaios-clinicos-radar/skills/buscar-ensaios-registrados/SKILL.md) | Use para localizar pesquisas registradas por condição, intervenção e local. |
| [`comparar-protocolos-ensaios`](../plugins/ensaios-clinicos-radar/skills/comparar-protocolos-ensaios/SKILL.md) | Use para comparar populações, intervenções e desfechos de protocolos. |
| [`organizar-fases-ensaios`](../plugins/ensaios-clinicos-radar/skills/organizar-fases-ensaios/SKILL.md) | Use para explicar e classificar fases e desenhos de estudos registrados. |
| [`verificar-status-ensaios`](../plugins/ensaios-clinicos-radar/skills/verificar-status-ensaios/SKILL.md) | Use para conferir recrutamento, conclusão e atualização de registros. |

### Imagem Médica Lab

[Documentação do plugin](../plugins/imagem-medica-lab/README.md) · Versão `0.1.0`

Inspecionar metadados DICOM, organizar séries, localizar bases públicas e avaliar qualidade técnica para pesquisa.

| Skill | Quando usar |
|---|---|
| [`avaliar-qualidade-imagem-pesquisa`](../plugins/imagem-medica-lab/skills/avaliar-qualidade-imagem-pesquisa/SKILL.md) | Use para verificar dimensões, artefatos técnicos e consistência de imagens para pesquisa. |
| [`buscar-bases-imagens-medicas`](../plugins/imagem-medica-lab/skills/buscar-bases-imagens-medicas/SKILL.md) | Use para localizar datasets públicos de radiologia ou patologia para estudo. |
| [`inspecionar-dicom`](../plugins/imagem-medica-lab/skills/inspecionar-dicom/SKILL.md) | Use para ler metadados técnicos de arquivos DICOM autorizados. |
| [`organizar-series-dicom`](../plugins/imagem-medica-lab/skills/organizar-series-dicom/SKILL.md) | Use para agrupar imagens em estudos e séries para pesquisa. |

### Genômica Explorer

[Documentação do plugin](../plugins/genomica-explorer/README.md) · Versão `0.1.0`

Consultar genes, reconciliar identificadores, comparar anotações e mapear vias para pesquisa.

| Skill | Quando usar |
|---|---|
| [`comparar-anotacoes-genomicas`](../plugins/genomica-explorer/skills/comparar-anotacoes-genomicas/SKILL.md) | Use para comparar funções ou coordenadas anotadas de genes e transcritos. |
| [`consultar-genes`](../plugins/genomica-explorer/skills/consultar-genes/SKILL.md) | Use para buscar informações de um gene em bases oficiais. |
| [`mapear-vias-biologicas`](../plugins/genomica-explorer/skills/mapear-vias-biologicas/SKILL.md) | Use para relacionar lista de genes a vias ou funções em bases de pesquisa. |
| [`reconciliar-identificadores-genomicos`](../plugins/genomica-explorer/skills/reconciliar-identificadores-genomicos/SKILL.md) | Use para mapear símbolos e IDs entre bases para pesquisa. |

## criacao

**Design, documentos e conteúdo**

### PostLab — Designer Criativo

[Documentação do plugin](../plugins/postlab/README.md) · Versão `0.3.0`

Designer de posts criativos com artes, fotos, legendas e carrosséis para redes sociais.

| Skill | Quando usar |
|---|---|
| [`adaptar-conteudo-canal`](../plugins/postlab/skills/adaptar-conteudo-canal/SKILL.md) | Use para reaproveitar mensagem em formatos textuais de redes distintas. |
| [`adaptar-formato-post`](../plugins/postlab/skills/adaptar-formato-post/SKILL.md) | Use para adaptar arte ou conteúdo entre formatos e redes sociais. |
| [`adaptar-newsletter`](../plugins/postlab/skills/adaptar-newsletter/SKILL.md) | Use para criar newsletter a partir de material verificável. |
| [`criar-posts-criativos`](../plugins/postlab/skills/criar-posts-criativos/SKILL.md) | Criar e refinar posts bonitos e criativos para Instagram, LinkedIn e outras redes, com direção de arte, imagens, legendas e carrosséis. Usar para design de post, arte para rede social, melhoria visual, campanha visual ou carrossel com identidade consistente. |
| [`criar-sequencia-posts`](../plugins/postlab/skills/criar-sequencia-posts/SKILL.md) | Use para dividir tema em série de publicações complementares. |
| [`manter-identidade-visual`](../plugins/postlab/skills/manter-identidade-visual/SKILL.md) | Use para criar guia visual ou aplicar consistência a uma série de posts. |
| [`planejar-carrossel`](../plugins/postlab/skills/planejar-carrossel/SKILL.md) | Use para roteirizar páginas de carrossel educativo ou profissional. |
| [`revisar-texto-arte`](../plugins/postlab/skills/revisar-texto-arte/SKILL.md) | Use para identificar erros de ortografia, conteúdo e legibilidade em imagem de post. |
| [`transformar-texto-roteiro`](../plugins/postlab/skills/transformar-texto-roteiro/SKILL.md) | Use para adaptar aula, artigo ou texto para roteiro de vídeo ou áudio. |

### LinkedIn Conteúdo Diário

[Documentação do plugin](../plugins/linkedin-conteudo-diario/README.md) · Versão `0.1.0`

Cria, valida e agenda lotes diários de posts educativos com imagens para LinkedIn.

| Skill | Quando usar |
|---|---|
| [`linkedin-conteudo-diario`](../plugins/linkedin-conteudo-diario/skills/linkedin-conteudo-diario/SKILL.md) | Cria e agenda lotes diários de posts educativos para LinkedIn sobre dados, Python, IA, machine learning, SQL, Excel e temas relacionados. Use quando o usuário pedir posts para LinkedIn, um lote diário, conteúdo com imagens ou publicação distribuída durante o dia. O padrão é cinco posts com imagens, horários de Brasília e uma aprovação explícita do lote antes do agendamento. |

### Resumo Visual Manuscrito

[Documentação do plugin](../plugins/resumo-visual-manuscrito/README.md) · Versão `0.1.1`

Transforma qualquer tema ou material de estudo em um resumo visual manuscrito, didático, organizado e focado em revisão de prova.

| Skill | Quando usar |
|---|---|
| [`criar-resumo-visual`](../plugins/resumo-visual-manuscrito/skills/criar-resumo-visual/SKILL.md) | Crie um resumo visual manuscrito premium sobre qualquer tema ou material fornecido, para compreensão rápida, revisão e memorização. Use quando o usuário pedir resumo visual, folha de estudos manuscrita, anotação de caderno, mapa visual de revisão ou material visual para prova. |

### VisualExplain

[Documentação do plugin](../plugins/visualexplain/README.md) · Versão `0.2.0`

Esqueleto para transformar materiais em explicações visuais animadas com roteiro e HTML.

| Skill | Quando usar |
|---|---|
| [`animar-processo-explicativo`](../plugins/visualexplain/skills/animar-processo-explicativo/SKILL.md) | Use para transformar um processo descrito em etapas visuais animadas em HTML. |
| [`criar-linha-tempo-visual`](../plugins/visualexplain/skills/criar-linha-tempo-visual/SKILL.md) | Use para explicar eventos históricos ou etapas temporais de um material. |
| [`explicar-visual-animado`](../plugins/visualexplain/skills/explicar-visual-animado/SKILL.md) | Transformar artigos, PDFs, slides, documentos e texto em explicações visuais animadas em HTML. Usar quando o usuário pedir aula visual, slide animado, explicação interativa ou transformação visual de um material. |
| [`incluir-quiz-visual`](../plugins/visualexplain/skills/incluir-quiz-visual/SKILL.md) | Use para adicionar perguntas objetivas e feedback em uma explicação HTML. |

### Documento Studio

[Documentação do plugin](../plugins/documento-studio/README.md) · Versão `0.1.0`

Criar relatórios, formatar documentos, preparar apresentações e revisar PDFs.

| Skill | Quando usar |
|---|---|
| [`criar-relatorio-documento`](../plugins/documento-studio/skills/criar-relatorio-documento/SKILL.md) | Use para estruturar e produzir relatório a partir de fatos e materiais fornecidos. |
| [`formatar-documento`](../plugins/documento-studio/skills/formatar-documento/SKILL.md) | Use para aplicar estilos, hierarquia, sumário, tabelas e paginação a um documento. |
| [`montar-apresentacao`](../plugins/documento-studio/skills/montar-apresentacao/SKILL.md) | Use para transformar material em roteiro ou arquivo de slides organizado. |
| [`revisar-pdf`](../plugins/documento-studio/skills/revisar-pdf/SKILL.md) | Use para verificar conteúdo, legibilidade, paginação e problemas visuais em PDF. |

## carreira

**Carreira, concursos e organização**

### Carreira Lab

[Documentação do plugin](../plugins/carreira-lab/README.md) · Versão `0.1.0`

Adaptar currículo, revisar perfil, praticar entrevista e mapear evidências de competências.

| Skill | Quando usar |
|---|---|
| [`adaptar-curriculo`](../plugins/carreira-lab/skills/adaptar-curriculo/SKILL.md) | Use para adaptar currículo ao anúncio sem inventar qualificações. |
| [`mapear-competencias-vaga`](../plugins/carreira-lab/skills/mapear-competencias-vaga/SKILL.md) | Use para comparar perfil e requisitos e planejar portfólio ou preparação. |
| [`revisar-perfil-linkedin`](../plugins/carreira-lab/skills/revisar-perfil-linkedin/SKILL.md) | Use para redigir título, Sobre e experiências de LinkedIn com base no histórico informado. |
| [`simular-entrevista`](../plugins/carreira-lab/skills/simular-entrevista/SKILL.md) | Use para praticar entrevista de emprego técnica ou comportamental com feedback. |

### Edital Fácil

[Documentação do plugin](../plugins/edital-facil/README.md) · Versão `0.2.0`

Lê editais de concursos e seleções e transforma requisitos, etapas, salários e prazos em um resumo e checklist prático.

| Skill | Quando usar |
|---|---|
| [`comparar-editais`](../plugins/edital-facil/skills/comparar-editais/SKILL.md) | Use para comparar seleções ou versões de um edital e identificar mudanças. |
| [`extrair-requisitos-edital`](../plugins/edital-facil/skills/extrair-requisitos-edital/SKILL.md) | Use para organizar escolaridade, experiência, documentos, cotas e condições de um edital. |
| [`ler-editais`](../plugins/edital-facil/skills/ler-editais/SKILL.md) | Analisa editais de concursos, seleções e residências para localizar cargos, requisitos, salários, etapas, cotas, documentos, prazos e regras de inscrição com referência ao texto original. |
| [`montar-checklist-edital`](../plugins/edital-facil/skills/montar-checklist-edital/SKILL.md) | Use para criar lista de documentos e ações de inscrição ou matrícula a partir de edital. |
| [`organizar-prazos-edital`](../plugins/edital-facil/skills/organizar-prazos-edital/SKILL.md) | Use para montar cronograma de inscrição, recursos, provas e resultados de um edital. |

### Arquivo Inteligente

[Documentação do plugin](../plugins/arquivo-inteligente/README.md) · Versão `0.1.0`

Inventariar arquivos, reconhecer duplicatas, propor nomes e organizar pastas com rastreabilidade.

| Skill | Quando usar |
|---|---|
| [`classificar-arquivos`](../plugins/arquivo-inteligente/skills/classificar-arquivos/SKILL.md) | Use para inventariar e classificar documentos por tipo, tema e finalidade. |
| [`detectar-arquivos-duplicados`](../plugins/arquivo-inteligente/skills/detectar-arquivos-duplicados/SKILL.md) | Use para encontrar arquivos com bytes iguais sem apagar originais. |
| [`padronizar-nomes-arquivos`](../plugins/arquivo-inteligente/skills/padronizar-nomes-arquivos/SKILL.md) | Use para propor ou aplicar renomeação consistente de arquivos. |
| [`planejar-pastas`](../plugins/arquivo-inteligente/skills/planejar-pastas/SKILL.md) | Use para propor estrutura de diretórios e migração de arquivos. |

### Reunião Clara

[Documentação do plugin](../plugins/reuniao-clara/README.md) · Versão `0.1.0`

Resumir transcrições, separar decisões, responsáveis e pendências.

| Skill | Quando usar |
|---|---|
| [`extrair-decisoes-reuniao`](../plugins/reuniao-clara/skills/extrair-decisoes-reuniao/SKILL.md) | Use para identificar decisões e critérios em uma transcrição. |
| [`identificar-responsaveis-reuniao`](../plugins/reuniao-clara/skills/identificar-responsaveis-reuniao/SKILL.md) | Use para mapear compromissos e responsáveis explicitamente atribuídos. |
| [`organizar-pendencias-reuniao`](../plugins/reuniao-clara/skills/organizar-pendencias-reuniao/SKILL.md) | Use para transformar assuntos abertos em lista de acompanhamento. |
| [`resumir-reuniao`](../plugins/reuniao-clara/skills/resumir-reuniao/SKILL.md) | Use para resumir uma transcrição ou notas de reunião. |

## desenvolvimento

**Plugins, GitHub e APIs**

### GitHub Organizer

[Documentação do plugin](../plugins/github-organizer/README.md) · Versão `0.2.0`

Melhorar README, gerar catálogo, registrar mudanças e conferir links.

| Skill | Quando usar |
|---|---|
| [`avaliar-impacto-alteracao`](../plugins/github-organizer/skills/avaliar-impacto-alteracao/SKILL.md) | Use para mapear consumidores e efeitos de mudança em código ou contrato. |
| [`catalogar-plugins`](../plugins/github-organizer/skills/catalogar-plugins/SKILL.md) | Use para gerar índice de plugins e skills a partir dos arquivos reais de um repositório. |
| [`escrever-changelog`](../plugins/github-organizer/skills/escrever-changelog/SKILL.md) | Use para documentar mudanças entre versões ou commits. |
| [`melhorar-readme`](../plugins/github-organizer/skills/melhorar-readme/SKILL.md) | Use para criar ou atualizar README de projeto com instruções verificáveis. |
| [`responder-feedback-codigo`](../plugins/github-organizer/skills/responder-feedback-codigo/SKILL.md) | Use para analisar comentários de code review e preparar correções ou respostas. |
| [`revisar-diff-codigo`](../plugins/github-organizer/skills/revisar-diff-codigo/SKILL.md) | Use para encontrar bugs e regressões em alterações de código. |
| [`verificar-links-repositorio`](../plugins/github-organizer/skills/verificar-links-repositorio/SKILL.md) | Use para encontrar links quebrados ou caminhos inexistentes na documentação. |
| [`verificar-pr-integracao`](../plugins/github-organizer/skills/verificar-pr-integracao/SKILL.md) | Use para conferir escopo, checks e condições antes de integrar pull request. |

### Skill Auditor

[Documentação do plugin](../plugins/skill-auditor/README.md) · Versão `0.1.0`

Avaliar estrutura, instruções, recursos e comportamento de skills com casos de uso.

| Skill | Quando usar |
|---|---|
| [`auditar-skill`](../plugins/skill-auditor/skills/auditar-skill/SKILL.md) | Use para revisar SKILL.md quanto a escopo, clareza, recursos e promessas. |
| [`avaliar-exemplos-skill`](../plugins/skill-auditor/skills/avaliar-exemplos-skill/SKILL.md) | Use para criar e executar casos que verifiquem comportamento real de uma skill. |
| [`revisar-limites-skill`](../plugins/skill-auditor/skills/revisar-limites-skill/SKILL.md) | Use para verificar tratamento de fontes, autorização, privacidade e dependências em workflows. |
| [`validar-estrutura-skill`](../plugins/skill-auditor/skills/validar-estrutura-skill/SKILL.md) | Use para verificar YAML, nome, referências e arquivos de uma skill. |

### Plugin Builder

[Documentação do plugin](../plugins/plugin-builder/README.md) · Versão `0.1.0`

Estruturar plugins de skills, preparar manifestos, documentar requisitos e empacotar versões.

| Skill | Quando usar |
|---|---|
| [`documentar-plugin`](../plugins/plugin-builder/skills/documentar-plugin/SKILL.md) | Use para escrever instruções de uso, configuração e limitações de um pacote. |
| [`empacotar-plugin`](../plugins/plugin-builder/skills/empacotar-plugin/SKILL.md) | Use para preparar arquivo ZIP ou tar.gz de plugin quando solicitado. |
| [`estruturar-plugin`](../plugins/plugin-builder/skills/estruturar-plugin/SKILL.md) | Use para organizar um plugin de skills ou integrar arquivos existentes em pacote. |
| [`preparar-manifesto-plugin`](../plugins/plugin-builder/skills/preparar-manifesto-plugin/SKILL.md) | Use para criar ou revisar plugin.json e overlays de compatibilidade. |

### API Explorer

[Documentação do plugin](../plugins/api-explorer/README.md) · Versão `0.1.0`

Ler documentação, realizar consultas autorizadas, paginar resultados e documentar respostas.

| Skill | Quando usar |
|---|---|
| [`documentar-resposta-api`](../plugins/api-explorer/skills/documentar-resposta-api/SKILL.md) | Use para produzir dicionário de campos e contrato a partir de documentação e respostas reais. |
| [`ler-documentacao-api`](../plugins/api-explorer/skills/ler-documentacao-api/SKILL.md) | Use para entender endpoints, autenticação, filtros e limites de uma API. |
| [`paginar-api`](../plugins/api-explorer/skills/paginar-api/SKILL.md) | Use para coletar várias páginas de resultados de uma API com controle de limites. |
| [`testar-consulta-api`](../plugins/api-explorer/skills/testar-consulta-api/SKILL.md) | Use para testar consulta HTTP de leitura a endpoint documentado. |

### Projeto do Zero

[Documentação do plugin](../plugins/projeto-do-zero/README.md) · Versão `0.1.0`

Refinar requisitos, definir aceite, dividir implementação e organizar dependências de um projeto.

| Skill | Quando usar |
|---|---|
| [`definir-aceite-projeto`](../plugins/projeto-do-zero/skills/definir-aceite-projeto/SKILL.md) | Use para escrever condições observáveis de conclusão de funcionalidades. |
| [`dividir-implementacao-projeto`](../plugins/projeto-do-zero/skills/dividir-implementacao-projeto/SKILL.md) | Use para transformar requisitos em tarefas pequenas com entregas. |
| [`mapear-dependencias-projeto`](../plugins/projeto-do-zero/skills/mapear-dependencias-projeto/SKILL.md) | Use para identificar bloqueios e sequência de entrega. |
| [`refinar-requisitos-projeto`](../plugins/projeto-do-zero/skills/refinar-requisitos-projeto/SKILL.md) | Use para transformar ideia em requisitos claros e verificáveis. |

### Debug Investigador

[Documentação do plugin](../plugins/debug-investigador/README.md) · Versão `0.1.0`

Reproduzir falhas, investigar causas, aplicar correções e verificar resultados em projetos diversos.

| Skill | Quando usar |
|---|---|
| [`corrigir-causa-falha`](../plugins/debug-investigador/skills/corrigir-causa-falha/SKILL.md) | Use para implementar correção mínima preservando comportamento. |
| [`investigar-causa-falha`](../plugins/debug-investigador/skills/investigar-causa-falha/SKILL.md) | Use para identificar causa raiz com hipóteses e evidências. |
| [`reproduzir-falha`](../plugins/debug-investigador/skills/reproduzir-falha/SKILL.md) | Use para construir reprodução mínima de erro ou comportamento inesperado. |
| [`verificar-correcao-falha`](../plugins/debug-investigador/skills/verificar-correcao-falha/SKILL.md) | Use para confirmar correção e avaliar regressões relevantes. |

### Release Manager

[Documentação do plugin](../plugins/release-manager/README.md) · Versão `0.1.0`

Verificar versões, preparar releases, planejar migração e reversão.

| Skill | Quando usar |
|---|---|
| [`planejar-migracao-release`](../plugins/release-manager/skills/planejar-migracao-release/SKILL.md) | Use para organizar atualização de usuários, formatos ou dados. |
| [`planejar-reversao-release`](../plugins/release-manager/skills/planejar-reversao-release/SKILL.md) | Use para definir rollback e condições de acionamento. |
| [`preparar-entrega-release`](../plugins/release-manager/skills/preparar-entrega-release/SKILL.md) | Use para produzir artefatos e notas de entrega verificáveis. |
| [`verificar-versao-release`](../plugins/release-manager/skills/verificar-versao-release/SKILL.md) | Use para conferir versão e compatibilidade antes de entrega. |

## financas

**Finanças e comparações**

### InvestIA — Análise de Investimentos

[Documentação do plugin](../plugins/investia/README.md) · Versão `0.2.0`

Pesquisa e compara investimentos com fundamentos, notícias, cenários e simulação de risco usando ferramentas disponíveis no ChatGPT.

| Skill | Quando usar |
|---|---|
| [`analisar-investimentos-ia`](../plugins/investia/skills/analisar-investimentos-ia/SKILL.md) | Analisar ações, ETFs, FIIs e criptoativos com fundamentos, demonstrações, notícias, análise técnica e gestão de risco. Usar para pesquisar um ativo, comparar investimentos, avaliar uma carteira ou simular tamanho de posição com IA. |
| [`comparar-ativos`](../plugins/investia/skills/comparar-ativos/SKILL.md) | Use para comparar ações, ETFs, FIIs ou outros ativos por critérios equivalentes. |
| [`ler-demonstracoes-financeiras`](../plugins/investia/skills/ler-demonstracoes-financeiras/SKILL.md) | Use para analisar DRE, balanço e fluxo de caixa de uma empresa. |
| [`simular-cenarios-investimento`](../plugins/investia/skills/simular-cenarios-investimento/SKILL.md) | Use para projetar cenários com aportes, retorno, inflação e custos declarados. |

### Comparador de carros

[Documentação do plugin](../plugins/comparador-precos-carros/README.md) · Versão `0.2.0`

Pesquisa e compara preços de carros no Brasil por categoria, marca, modelo, versão e região, com fontes e critérios claros.

| Skill | Quando usar |
|---|---|
| [`checklist-avaliar-carro`](../plugins/comparador-precos-carros/skills/checklist-avaliar-carro/SKILL.md) | Use para orientar inspeção documental e visual antes de compra de usado. |
| [`comparar-precos-carros`](../plugins/comparador-precos-carros/skills/comparar-precos-carros/SKILL.md) | Pesquisa e compara preços de carros no Brasil por categoria, marca, modelo, versão, ano e região. Use quando a pessoa quiser encontrar veículos dentro de um orçamento, comparar carros novos ou usados, consultar preço de mercado ou FIPE, ou avaliar consumo e custos de uso. |
| [`comparar-versoes-carro`](../plugins/comparador-precos-carros/skills/comparar-versoes-carro/SKILL.md) | Use para comparar equipamentos, motorização, segurança e preço por versão/ano. |
| [`estimar-custo-carro`](../plugins/comparador-precos-carros/skills/estimar-custo-carro/SKILL.md) | Use para estimar gasto mensal e anual de veículo com parâmetros locais. |

### TokenMeter Universal

[Documentação do plugin](../plugins/tokenmeter-universal/README.md) · Versão `1.0.0`

Registro portátil de consumo de tokens com relatórios diários, semanais, mensais, anuais e total acumulado. Importação de metadados, custos configuráveis e MCP local.

| Skill | Quando usar |
|---|---|
| [`medir-tokens`](../plugins/tokenmeter-universal/skills/medir-tokens/SKILL.md) | Medir e registrar tokens de IA por dia, semana, mês, ano e total acumulado. Usar para auditoria de consumo, importação CSV/JSON/JSONL, metadados OpenAI/compatíveis, Claude, Gemini e Ollama, custos configuráveis e estimativas de texto. |

### Recibos & Despesas

[Documentação do plugin](../plugins/recibos-despesas/README.md) · Versão `0.1.0`

Extrair recibos, categorizar gastos, identificar duplicidades e consolidar valores com origem.

| Skill | Quando usar |
|---|---|
| [`categorizar-despesas`](../plugins/recibos-despesas/skills/categorizar-despesas/SKILL.md) | Use para agrupar gastos por categoria com regras explícitas. |
| [`conferir-duplicidades-recibos`](../plugins/recibos-despesas/skills/conferir-duplicidades-recibos/SKILL.md) | Use para identificar possíveis lançamentos repetidos em despesas. |
| [`consolidar-despesas`](../plugins/recibos-despesas/skills/consolidar-despesas/SKILL.md) | Use para somar lançamentos normalizados por mês, categoria e moeda. |
| [`extrair-dados-recibos`](../plugins/recibos-despesas/skills/extrair-dados-recibos/SKILL.md) | Use para ler recibos e registrar valores, datas e origem. |
