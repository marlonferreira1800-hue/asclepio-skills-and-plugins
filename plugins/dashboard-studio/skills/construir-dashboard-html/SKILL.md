---
name: construir-dashboard-html
description: "Construir dashboard interativo em HTML autossuficiente com gráficos (Chart.js), filtros dinâmicos, cards de KPI e tabelas ordenáveis."
---

# Construir dashboard interativo em HTML

Esta habilidade orienta a criação de painéis analíticos interativos autossuficientes em arquivo único HTML5, com gráficos dinâmicos via Chart.js, filtros reativos em JavaScript puro, cards de indicadores-chave (KPIs) e tabelas de dados ordenáveis. O arquivo roda diretamente no navegador, sem necessidade de servidor local ou dependências instaladas.

## Entradas

1. **Objetivo do painel**: Visão executiva, monitoramento operacional ou diagnóstico aprofundado.
2. **Público-alvo**: Diretoria, líderes de equipe ou analistas técnicos.
3. **Métricas e KPIs essenciais**: Indicadores principais, metas, comparativos com período anterior.
4. **Dimensões de filtro**: Segmentação por período, categoria, região ou status.
5. **Fonte ou formato dos dados**: Dados tabulares (CSV, JSON), resultados de consulta SQL ou especificação para geração de dados simulados realistas.

## Fluxo

1. **Definição de escopo e hierarquia**: Identificar 2 a 4 KPIs de destaque para o topo, 2 a 4 gráficos analíticos para a área central e 1 tabela de detalhamento na base.
2. **Estruturação dos dados**: Limpar e converter a base em estrutura JSON embutida no próprio script HTML (`const DADOS = [...]`), garantindo funcionamento 100% offline.
3. **Composição visual e semântica**: Estruturar HTML5 semântico com cabeçalho de filtros, linha de cards de KPI, grade de gráficos e container de tabela.
4. **Instanciação dos gráficos**: Configurar instâncias do Chart.js com paleta harmônica, contraste acessível, formatação de eixos e tooltips explicativos.
5. **Interatividade e reatividade**: Ligar eventos `onchange` e `input` dos filtros a uma classe gerenciadora que recalcula KPIs, atualiza gráficos via `chart.update('none')` e filtra linhas da tabela sem reconstruir o DOM.
6. **Polimento responsivo**: Aplicar CSS Grid e Flexbox com quebras automáticas para visualização confortável em telas amplas, notebooks e dispositivos móveis.

## Arquitetura e template base

Todo dashboard autossuficiente adota a seguinte arquitetura limpa em arquivo único:

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Painel Analítico</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.1"></script>
    <style>
      :root {
        --bg-principal: #f8f9fa;
        --bg-card: #ffffff;
        --bg-topo: #1e293b;
        --texto-principal: #0f172a;
        --texto-secundario: #64748b;
        --texto-claro: #ffffff;
        --primaria: #2563eb;
        --sucesso: #16a34a;
        --alerta: #ea580c;
        --perigo: #dc2626;
        --borda: #e2e8f0;
        --espaco: 16px;
        --raio: 8px;
      }
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family:
          -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      }
      body {
        background: var(--bg-principal);
        color: var(--texto-principal);
        line-height: 1.5;
        padding: var(--espaco);
      }
      .container {
        max-width: 1400px;
        margin: 0 auto;
      }
      .cabecalho {
        background: var(--bg-topo);
        color: var(--texto-claro);
        padding: 20px 24px;
        border-radius: var(--raio);
        margin-bottom: var(--espaco);
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 12px;
      }
      .cabecalho h1 {
        font-size: 20px;
        font-weight: 700;
      }
      .filtros {
        display: flex;
        gap: 12px;
        align-items: center;
        flex-wrap: wrap;
      }
      .filtro-item {
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: 13px;
      }
      .filtro-item select,
      .filtro-item input {
        padding: 6px 10px;
        border-radius: 4px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: rgba(255, 255, 255, 0.1);
        color: #fff;
        font-size: 13px;
      }
      .kpi-grade {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: var(--espaco);
        margin-bottom: var(--espaco);
      }
      .kpi-card {
        background: var(--bg-card);
        border-radius: var(--raio);
        padding: 18px 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
        border: 1px solid var(--borda);
      }
      .kpi-titulo {
        font-size: 12px;
        text-transform: uppercase;
        color: var(--texto-secundario);
        font-weight: 600;
        margin-bottom: 6px;
      }
      .kpi-valor {
        font-size: 26px;
        font-weight: 700;
        color: var(--texto-principal);
        margin-bottom: 4px;
      }
      .kpi-var {
        font-size: 12px;
        font-weight: 600;
      }
      .kpi-var.positivo {
        color: var(--sucesso);
      }
      .kpi-var.negativo {
        color: var(--perigo);
      }
      .graficos-grade {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
        gap: var(--espaco);
        margin-bottom: var(--espaco);
      }
      .grafico-card {
        background: var(--bg-card);
        border-radius: var(--raio);
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
        border: 1px solid var(--borda);
        height: 350px;
        display: flex;
        flex-direction: column;
      }
      .grafico-card h3 {
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 14px;
      }
      .grafico-card canvas {
        flex: 1;
        max-height: 280px;
      }
      .tabela-card {
        background: var(--bg-card);
        border-radius: var(--raio);
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
        border: 1px solid var(--borda);
        overflow-x: auto;
      }
      table {
        width: 100%;
        border-collapse: collapse;
        font-size: 13px;
      }
      th {
        text-align: left;
        padding: 10px 12px;
        border-bottom: 2px solid var(--borda);
        color: var(--texto-secundario);
        cursor: pointer;
        user-select: none;
      }
      td {
        padding: 10px 12px;
        border-bottom: 1px solid var(--borda);
      }
      tr:hover td {
        background: #f1f5f9;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <header class="cabecalho">
        <h1>Painel de Desempenho</h1>
        <div class="filtros" id="area-filtros"></div>
      </header>
      <section class="kpi-grade" id="area-kpis"></section>
      <section class="graficos-grade">
        <div class="grafico-card">
          <h3>Evolução Temporal</h3>
          <canvas id="grafico-linha"></canvas>
        </div>
        <div class="grafico-card">
          <h3>Comparativo por Categoria</h3>
          <canvas id="grafico-barra"></canvas>
        </div>
      </section>
      <section class="tabela-card">
        <table id="tabela-dados"></table>
      </section>
    </div>
    <script>
      const PALETA = [
        "#2563eb",
        "#0891b2",
        "#0d9488",
        "#16a34a",
        "#ca8a04",
        "#dc2626",
      ];
      // Gerenciador reativo
      class PainelApp {
        constructor(dados) {
          this.brutos = dados;
          this.filtrados = dados;
          this.graficos = {};
          this.init();
        }
        init() {
          this.renderFiltros();
          this.renderKPIs();
          this.renderGraficos();
          this.renderTabela();
        }
        filtrar() {
          // Aplica regras de seleção e atualiza componentes
        }
        renderFiltros() {
          /* preenche selects */
        }
        renderKPIs() {
          /* atualiza números */
        }
        renderGraficos() {
          /* instancia Chart.js */
        }
        renderTabela() {
          /* desenha linhas */
        }
      }
    </script>
  </body>
</html>
```

## Padrões de gráficos no Chart.js

1. **Linha contínua (Série Temporal)**:
   - Configurar `tension: 0.3` para curva suave.
   - Usar preenchimento sutil `backgroundColor: hex + '15'`.
   - Adicionar `interaction: { mode: 'index', intersect: false }` para tooltip conjunto no mesmo ponto x.
2. **Barras horizontais (Ranking de Categorias)**:
   - Configurar `indexAxis: 'y'` para categorias com nomes longos.
   - Definir `borderRadius: 4` para cantos modernos.
   - Começar o eixo numérico em zero obrigatoriamente (`beginAtZero: true`).
3. **Donut / Rosca (Composição Parte-Todo)**:
   - Utilizar apenas quando houver 6 ou menos categorias.
   - Definir `cutout: '65%'` para estética clean com espaço respirável.
4. **Atualização sem recriação**:
   - Atualizar dados de gráficos existentes com `chart.data.labels = novosLabels; chart.data.datasets[0].data = novosValores; chart.update('none');`. Evita vazamento de memória e piscar de tela.

## Tabela ordenável e paginação

- Incorporar função de ordenação bidirecional (`asc`/`desc`) em clique nos cabeçalhos `<th>`.
- Limitar tabelas a 50 ou 100 linhas por página em dados volumosos para manter o navegador fluido.
- Formatar valores numéricos, moedas (R$ 1.250,00) e percentuais com `Intl.NumberFormat('pt-BR')`.

## Desempenho e agregação

| Volume de registros   | Abordagem recomendada                                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Até 2.000 linhas      | Embutir registros brutos em JSON no arquivo HTML. Filtragem dinâmica instantânea no navegador.                        |
| 2.000 a 50.000 linhas | Pré-agregar dados em agrupamentos mensais/categoriais antes de gerar o HTML para evitar sobrecarga de memória.        |
| Mais de 50.000 linhas | Criar resumos de métricas pré-calculados para exibição no painel e fornecer link de download do extrato bruto em CSV. |

## Entrega

Arquivo `.html` completo, válido, visualmente refinado, responsivo e autônomo, pronto para abertura direta com duplo clique em qualquer navegador (Chrome, Edge, Firefox, Safari).

## Verificação e limites

- Não depender de servidores Node, Flask ou APIs ativas: o painel deve ser 100% estático e funcional por si só.
- Garantir que as bibliotecas CDN (como Chart.js) usem versões estáveis e possuam fallback ou estrutura graciosa caso esteja offline.
- Separar wireframe de código executável. Testar se o arquivo abre sem erros no console JavaScript.

## Exemplos

- Construa um painel de vendas mensais em HTML com KPI de faturamento, gráfico de barras por canal e tabela de pedidos com filtros de data.
- Gere um dashboard operacional com volume de chamados por prioridade, tempo médio de resposta e taxa de resolução em Chart.js.
