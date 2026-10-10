# Comparador de preços de carros

Plugin privado com uma skill que pesquisa e compara carros no Brasil por categoria, marca, versão, ano e região. Diferencia preço sugerido, preço anunciado e FIPE, inclui links das fontes e evita preencher dados ausentes com estimativas ocultas.

## Estrutura

- `plugin.json`: identificação e apresentação do plugin.
- `skills/comparar-precos-carros/SKILL.md`: fluxo de pesquisa e comparação.
- `skills/comparar-precos-carros/agents/openai.yaml`: nome e prompt da skill na interface.

## Exemplo

“Compare SUVs usados até R$ 80 mil em Jaru (RO), econômicos para cidade e com manutenção acessível.”

## Skills desta ampliação

| Skill                                                                | Função                                   |
| -------------------------------------------------------------------- | ---------------------------------------- |
| [`estimar-custo-carro`](skills/estimar-custo-carro/SKILL.md)         | Estimar custo de uso de carro            |
| [`comparar-versoes-carro`](skills/comparar-versoes-carro/SKILL.md)   | Comparar versões de carro                |
| [`checklist-avaliar-carro`](skills/checklist-avaliar-carro/SKILL.md) | Preparar checklist de avaliação de carro |

## Requisitos e execução

Fontes de preços, fabricante, PBE/Inmetro e regras locais; orçamento com premissas declaradas.

Este pacote fornece instruções reutilizáveis. Não cria conexões, assinaturas, publicação ou execução automática. Os scripts incluídos estão documentados nas skills que os utilizam.

## Exemplos

- Estime o custo mensal deste carro rodando 1.000 km em Rondônia.
- Compare as versões deste modelo e diga o que muda entre elas.
- Monte um checklist para avaliar este carro usado antes da compra.
