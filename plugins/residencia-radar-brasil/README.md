# Residência Radar Brasil

Pesquisa e compara programas de residência médica por especialidade, instituição, estado e processo seletivo.

## O que faz

- Localiza editais, retificações, resultados, convocações e listas de espera.
- Compara vagas, relação candidato/vaga, notas e chamadas entre instituições e edições.
- Separa ampla concorrência e reserva PcD quando o documento oficial publica esses dados.
- Organiza os resultados em tabelas com ano, etapa, critério de classificação e links diretos.
- Sinaliza dados ausentes ou incomparáveis sem estimar valores.

## Como usar

Informe especialidade, região ou instituições, processo seletivo e edição desejada. Exemplo:

> “Compare as vagas de Radiologia do ENARE por estado, incluindo vagas PcD quando constarem no edital.”

## Fontes e limites

Priorize páginas oficiais do ENARE/Ebserh, instituições, universidades e bancas organizadoras. Cada nota ou convocação deve ser identificada pela edição e etapa. A relação candidato/vaga só deve ser calculada quando houver números oficiais de inscritos e vagas compatíveis. Dados PcD devem seguir o edital e não podem ser inferidos de listas incompletas.

Este plugin fornece pesquisa educacional e organização de informações públicas; não prevê aprovação nem substitui o edital.

## Skills desta ampliação

| Skill                                                                              | Função                            |
| ---------------------------------------------------------------------------------- | --------------------------------- |
| [`comparar-vagas-residencia`](skills/comparar-vagas-residencia/SKILL.md)           | Comparar vagas de residência      |
| [`comparar-ampla-pcd`](skills/comparar-ampla-pcd/SKILL.md)                         | Comparar ampla concorrência e PcD |
| [`organizar-notas-residencia`](skills/organizar-notas-residencia/SKILL.md)         | Organizar notas de residência     |
| [`acompanhar-chamadas-residencia`](skills/acompanhar-chamadas-residencia/SKILL.md) | Organizar chamadas de residência  |

## Requisitos e execução

Fontes oficiais de editais, resultados e convocações; pesquisa web necessária para consultas atuais.

Este pacote fornece instruções reutilizáveis. Não cria conexões, assinaturas, publicação ou execução automática. Os scripts incluídos estão documentados nas skills que os utilizam.

## Exemplos

- Compare vagas de Radiologia por instituição e estado.
- Compare a nota do último convocado na ampla e PcD em Radiologia.
- Ordene as notas finais PcD destas instituições da menor para a maior.
- Veja até qual classificação a lista de Radiologia rodou nesta edição.
