# Dados de Saúde Brasil

Plugin de pesquisa simples de notificações, internações e óbitos por doença em fontes públicas oficiais do SUS.

## Como usar

Informe a doença, a cidade ou estado e o ano. Exemplo: “Pesquise dengue em Jaru/RO em 2024”.

## O que consulta

- SINAN: notificações e classificações dos casos.
- SIH/SUS: internações processadas pelo SUS.
- SIM: óbitos registrados.

A resposta apresenta os totais em uma tabela curta, com links das fontes e observações sobre atualização ou limitações. A skill diferencia notificações de casos confirmados e não estima números indisponíveis.

## Fontes

- [Portal de Dados Abertos do SUS](https://dadosabertos.saude.gov.br/)
- [API de Dados Abertos do Ministério da Saúde](https://apidadosabertos.saude.gov.br/)
- [DATASUS/TABNET](https://datasus.saude.gov.br/)

## Estrutura

- `plugin.json`: manifesto portátil.
- `.codex-plugin/plugin.json`: manifesto de compatibilidade.
- `skills/consulta-dados-doencas/SKILL.md`: instruções para pesquisar e apresentar os dados.

Este é um plugin de instruções: a consulta depende dos recursos de pesquisa e acesso a fontes disponíveis no assistente. Não contém banco de dados próprio nem acesso a dados pessoais de pacientes.
