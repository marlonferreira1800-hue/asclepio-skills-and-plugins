---
name: visualizacao-dados
description: "Selecionar gráficos ideais e gerar visualizações de dados profissionais e acessíveis com Python."
---

# Visualização de dados profissional

Esta habilidade orienta a seleção técnica rigorosa de gráficos, boas práticas de design visual, acessibilidade (inclusão para daltonismo) e padrões de código em Python (Matplotlib, Seaborn e Plotly) para criação de figuras de qualidade de publicação e relatórios corporativos de alto nível.

## Entradas

1. **Conjunto de dados**: Tabela estruturada, DataFrame do Pandas, consulta SQL ou arquivo CSV/Excel.
2. **Pergunta de negócio ou hipótese analítica**: O que o gráfico deve responder (tendência, comparação, distribuição, correlação, ranking ou composição).
3. **Público e contexto**: Relatório técnico, apresentação executiva, artigo científico ou aplicação web interativa.
4. **Restrições de formato**: Estático de alta resolução (PNG/PDF em 150-300 DPI) ou interativo em navegador (HTML/Plotly).

## Fluxo

1. **Classificação da relação analítica**: Mapear as variáveis (temporais, categóricas, contínuas, geográficas) e determinar a família de gráfico mais precisa.
2. **Eliminação de ruído e antipadrões**: Descartar gráficos 3D, evitar gráficos de pizza com muitas fatias e garantir escala proporcional.
3. **Construção do código**: Utilizar padrões consolidados com estilo visual limpo, títulos acionáveis que comunicam a conclusão e rótulos com unidades claras.
4. **Aplicação de paleta acessível**: Garantir que as séries sejam distinguíveis por daltônicos (paletas Okabe-Ito, ColorBrewer ou pares azul/laranja) e por formas/estilos de linha.
5. **Ajuste fino de tipografia e respiro**: Evitar inclinação de 90° em rótulos de eixos (usar barras horizontais se houver muitas categorias), remover bordas desnecessárias (_spines_ superior e direita).
6. **Exportação**: Salvar com `bbox_inches='tight'` e resolução adequada para o canal de entrega.

## Guia de seleção de gráficos por relação de dados

| O que você deseja mostrar              | Gráfico principal recomendado          | Alternativas válidas                                    |
| -------------------------------------- | -------------------------------------- | ------------------------------------------------------- |
| **Tendência temporal**                 | Gráfico de linha                       | Gráfico de área (para volumes acumulados)               |
| **Comparação entre categorias**        | Gráfico de barras verticais            | Barras horizontais, gráfico de pirulito (_lollipop_)    |
| **Ranking / Classificação**            | Gráfico de barras horizontais          | Gráfico de pontos (_dot plot_), slope chart             |
| **Composição parte-todo**              | Barras empilhadas (_stacked bar_)      | Treemap (hierárquico), gráfico de waffle                |
| **Composição ao longo do tempo**       | Área empilhada (_stacked area_)        | Barras 100% empilhadas                                  |
| **Distribuição de variável contínua**  | Histograma                             | Boxplot, gráfico de violino (_violin plot_), strip plot |
| **Correlação (2 variáveis numéricas)** | Gráfico de dispersão (_scatter plot_)  | Gráfico de bolhas (3ª variável no raio)                 |
| **Correlação multivariada**            | Matriz de calor (_heatmap_)            | Matriz de pares (_pairplot_)                            |
| **Padrões geográficos**                | Mapa coroplético                       | Mapa de bolhas ou mapa hexagonal                        |
| **Fluxo, etapas ou funil**             | Diagrama de Sankey                     | Gráfico de funil (fases sequenciais)                    |
| **Redes de relacionamentos**           | Grafo de rede (_network graph_)        | Diagrama de cordas (_chord diagram_)                    |
| **Desempenho vs. Meta**                | Gráfico de balas (_bullet chart_)      | Indicador velocímetro (_gauge_ apenas para 1 KPI)       |
| **Múltiplos KPIs simultâneos**         | Pequenos múltiplos (_small multiples_) | Painel com gráficos em grade independente               |

### Antipadrões proibidos

- **Gráficos 3D**: Proibidos. Distorcem a percepção das proporções e não agregam informação.
- **Gráficos de pizza com mais de 5 categorias**: O cérebro humano tem dificuldade para comparar ângulos e áreas curvas. Prefira barras horizontais ordenadas.
- **Barras sem base zero**: Gráficos de barras devem SEMPRE iniciar o eixo de valores em zero para não exagerar diferenças visuais. Gráficos de linha podem ter base móvel quando a variação sutil for o foco.
- **Eixos duplos desalinhados**: Use com extrema cautela, pois frequentemente sugerem falsa correlação. Em vez disso, use dois gráficos empilhados compartilhando o eixo X.

## Padrões de código em Python

### 1. Configuração base (Matplotlib / Seaborn)

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import pandas as pd

# Estilo profissional limpo
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'figure.figsize': (10, 6),
    'figure.dpi': 150,
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
})

# Paleta amigável para daltônicos
PALETA_CATEGORICA = ['#2563eb', '#d97706', '#059669', '#dc2626', '#7c3aed', '#9333ea']
```

### 2. Barras horizontais com ranking ordenado

```python
fig, ax = plt.subplots(figsize=(10, 6))
df_ord = df.sort_values('valor', ascending=True)

barras = ax.barh(df_ord['categoria'], df_ord['valor'], color=PALETA_CATEGORICA[0], height=0.6)

# Rótulo de valores direto nas barras
for barra in barras:
    w = barra.get_width()
    ax.text(w + (df_ord['valor'].max() * 0.01), barra.get_y() + barra.get_height()/2,
            f'{w:,.0f}', ha='left', va='center', fontsize=10, fontweight='bold')

ax.set_title('Faturamento por Linha de Produto (Ranking)', pad=15)
ax.set_xlabel('Valor Total (R$)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('ranking_produtos.png', dpi=150, bbox_inches='tight')
```

### 3. Gráficos interativos com Plotly

```python
import plotly.express as px

fig = px.line(df, x='data', y='faturamento', color='canal',
              title='<b>Evolução Diária de Faturamento por Canal</b>',
              labels={'faturamento': 'Faturamento (R$)', 'data': 'Data', 'canal': 'Canal'},
              color_discrete_sequence=PALETA_CATEGORICA)

fig.update_layout(
    hovermode='x unified',
    plot_bgcolor='white',
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
)
fig.write_html('faturamento_interativo.html')
```

## Princípios de acessibilidade visual

1. **Distinção não dependente apenas da cor**: Combinar cor com espessuras de linha, marcadores (círculos, triângulos, quadrados) e padrões de traço (sólido, tracejado).
2. **Contraste mínimo**: Seguir taxa de contraste WCAG AA de pelo menos 4.5:1 entre elementos gráficos e o fundo.
3. **Títulos descritivos da conclusão**: Em vez de _"Vendas por Região"_, utilizar títulos informativos como _"Região Sudeste lidera expansão com 42% do volume total"_.

## Entrega

Script Python executável acompanhado de imagem renderizada (`.png`/`.svg`) ou arquivo interativo autônomo (`.html`), com justificativa da escolha gráfica e parâmetros aplicados.

## Verificação e limites

- Assegurar que os eixos estejam explicitamente identificados com unidades de medida (R$, %, unidades).
- Não omitir fontes de dados nem períodos observados.
- Testar legibilidade dos rótulos em telas menores antes de aprovar a visualização final.

## Exemplos

- Crie um gráfico comparando a distribuição salarial entre áreas de tecnologia usando boxplots e violin plots com Seaborn.
- Gere uma visualização temporal com Plotly mostrando o crescimento mensal de clientes com linha de média móvel e anotações dos marcos de lançamento.
