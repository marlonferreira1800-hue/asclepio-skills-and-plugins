# InvestIA — Análise de Investimentos

Plugin de instruções para pesquisar ações, ETFs, FIIs e criptoativos em português do Brasil. Reúne fundamentos, demonstrações, notícias, cenários e riscos com fontes verificáveis.

## Conteúdo

- `plugin.json`: manifesto portátil.
- `.codex-plugin/plugin.json`: compatibilidade Codex.
- `skills/analisar-investimentos-ia/SKILL.md`: fluxo de análise.
- `references/metodo.md`: critérios por classe de ativo.
- `scripts/position_size.py`: calculadora de posição para compra à vista.

## Exemplos

- Analise PETR4 com fontes atuais, fundamentos, notícias e riscos.
- Compare dois ETFs por taxas, concentração e exposição cambial.
- Avalie os riscos de uma carteira enviada em CSV.

## Simulação de posição

Requer Python 3, sem dependências externas:

```bash
python3 skills/analisar-investimentos-ia/scripts/position_size.py \
  --capital 10000 --risk-pct 1 --entry 20 --stop 18 --max-allocation-pct 20
```

O exemplo fictício retorna 50 unidades, R$ 1.000 alocados e R$ 100 de risco nominal. Pode-se informar `--lot 100` para arredondar a lotes de 100 unidades. Se nenhum lote respeitar os limites, a quantidade será zero.

## Uso e limites

Importe o pacote em um cliente compatível ou copie a pasta da skill para o diretório de skills indicado pelo cliente. Pesquisa e cotações dependem das ferramentas disponíveis no assistente. Este pacote não inclui API própria, credenciais, servidor MCP, conexão com corretora, envio de ordens ou monitoramento contínuo. A calculadora não cobre opções, futuros, alavancagem ou venda a descoberto. Taxas, gaps e slippage podem aumentar a perda além da simulação.

Análises e cenários são educacionais; dividendos e retornos não são garantidos. Licença MIT conforme o repositório.

## Skills desta ampliação

| Skill                                                                            | Função                           |
| -------------------------------------------------------------------------------- | -------------------------------- |
| [`comparar-ativos`](skills/comparar-ativos/SKILL.md)                             | Comparar ativos financeiros      |
| [`ler-demonstracoes-financeiras`](skills/ler-demonstracoes-financeiras/SKILL.md) | Ler demonstrações financeiras    |
| [`simular-cenarios-investimento`](skills/simular-cenarios-investimento/SKILL.md) | Simular cenários de investimento |

## Requisitos e execução

Fontes oficiais de emissores, CVM e mercado; cotações com data/hora. Simulação educacional, sem execução de ordens.

Este pacote fornece instruções reutilizáveis. Não cria conexões, assinaturas, publicação ou execução automática. Os scripts incluídos estão documentados nas skills que os utilizam.

## Exemplos

- Compare PETR4 e VALE3 com fundamentos e riscos atuais.
- Analise estas demonstrações e explique a geração de caixa.
- Simule aportes mensais com três cenários de retorno e inflação.
