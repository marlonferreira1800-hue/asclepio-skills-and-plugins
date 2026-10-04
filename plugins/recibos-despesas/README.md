# Recibos & Despesas

Extrair recibos, categorizar gastos, identificar duplicidades e consolidar valores com origem.

## Skills desta ampliação

| Skill | Função |
|---|---|
| [`extrair-dados-recibos`](skills/extrair-dados-recibos/SKILL.md) | Extrair dados de recibos |
| [`categorizar-despesas`](skills/categorizar-despesas/SKILL.md) | Categorizar despesas |
| [`conferir-duplicidades-recibos`](skills/conferir-duplicidades-recibos/SKILL.md) | Conferir duplicidades de recibos |
| [`consolidar-despesas`](skills/consolidar-despesas/SKILL.md) | Consolidar despesas |

## Requisitos e execução

PDF/imagem e ferramenta de OCR quando necessário; Python padrão para consolidar JSON normalizado. Sem conexão bancária ou aconselhamento tributário.

Este pacote fornece instruções reutilizáveis. Não cria conexões, assinaturas, publicação ou execução automática. Os scripts incluídos estão documentados nas skills que os utilizam.

## Exemplos

- Extraia datas e totais destes recibos com o arquivo de origem.
- Separe estas despesas em alimentação, transporte e estudo.
- Veja quais recibos parecem repetidos antes de consolidar.
- Consolide estes recibos em uma tabela mensal de despesas.
