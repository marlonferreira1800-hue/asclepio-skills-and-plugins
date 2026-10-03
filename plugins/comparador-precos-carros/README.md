# Comparador de preços de carros

Plugin privado com uma skill que pesquisa e compara carros no Brasil por categoria, marca, versão, ano e região. Diferencia preço sugerido, preço anunciado e FIPE, inclui links das fontes e evita preencher dados ausentes com estimativas ocultas.

## Estrutura

- `plugin.json`: identificação e apresentação do plugin.
- `skills/comparar-precos-carros/SKILL.md`: fluxo de pesquisa e comparação.
- `skills/comparar-precos-carros/agents/openai.yaml`: nome e prompt da skill na interface.

## Exemplo

“Compare SUVs usados até R$ 80 mil em Jaru (RO), econômicos para cidade e com manutenção acessível.”
