---
name: consulta-dados-doencas
description: Pesquisa notificações, casos, internações e óbitos por doença em município, estado ou Brasil usando fontes públicas oficiais. Use quando o usuário pedir dados, estatísticas ou uma consulta epidemiológica simples.
---

# Consultar dados de doenças

Faça a pesquisa por doença, localidade e período com o mínimo de etapas para o usuário.

## Procedimento

1. Identifique doença, localidade e ano/período. Se faltar algo essencial, faça uma pergunta curta. Se a pessoa disser “mais recente”, use o período mais novo disponível e informe qual é.
2. Comece pelas fontes públicas oficiais do Ministério da Saúde e do DATASUS. Use os conjuntos de dados do Portal de Dados Abertos do SUS ou sua API. Se não houver consulta direta, use o arquivo oficial CSV/JSON ou o TABNET.
3. Escolha a base conforme o indicador:
   - SINAN: notificações e classificações dos casos;
   - SIH/SUS: internações financiadas/processadas pelo SUS;
   - SIM: óbitos registrados.
4. Confira se a contagem é por município de residência ou por local do atendimento/internação. Informe o critério quando disponível.
5. Confirme atualização, período, definições e possíveis revisões da base. Não invente números, endpoints ou datas. Diferencie “zero registros” de “dado indisponível”.

## Resposta prática

Comece pela resposta e use uma tabela curta:

| Indicador | Total |
|---|---:|
| Notificações | ... |
| Casos confirmados, se disponíveis | ... |
| Internações | ... |
| Óbitos | ... |

Depois, informe os links diretos das fontes e uma observação breve sobre atualização ou limitação. Se não encontrar um valor, escreva “não localizado na fonte consultada”; não estime.

## Fontes de referência

- Portal de Dados Abertos do SUS: https://dadosabertos.saude.gov.br/
- API de Dados Abertos do Ministério da Saúde: https://apidadosabertos.saude.gov.br/
- DATASUS/TABNET: https://datasus.saude.gov.br/
- Internações SIH/SUS: https://datasus.saude.gov.br/acesso-a-informacao/morbidade-hospitalar-do-sus-sih-sus/

Use somente dados públicos agregados. Não tente identificar pacientes nem interprete estatísticas populacionais como diagnóstico individual.
