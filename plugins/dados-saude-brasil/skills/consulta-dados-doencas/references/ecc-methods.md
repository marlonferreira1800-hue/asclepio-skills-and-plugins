# Métodos ECC adaptados para dados-saude-brasil

## Arquitetura aplicada

Usar a skill existente como entrada e carregar esta referência somente quando planejar ou revisar a tarefa correspondente. Preservar os scripts, modelos, recursos e integrações do fluxo original. Não ativar hooks, agentes, comandos ou serviços do ECC automaticamente.

Aplicar as etapas desta referência como planejamento e revisão pelo próprio assistente. Não afirmar que especialistas ou agentes independentes foram executados. As instruções do usuário e as regras do ambiente continuam prevalecendo.

## Revisão proporcional

Conferir adequação ao pedido, precisão, fontes necessárias, consistência e formato. Corrigir falhas antes de entregar. Relatar verificações somente quando executadas e distinguir revisão de texto, execução de código, inspeção visual e comportamento no aplicativo.

## Procedimento específico

1. Manter um contrato de consulta: doença, código/classificação quando disponível, município/UF, período, base e critério territorial.
2. Executar busca inicial, avaliar se a base responde ao indicador e refinar somente as lacunas, em até três ciclos. Não repetir buscas que já produziram o dado necessário.
3. Registrar origem e data de atualização por indicador. Conferir filtros aplicados, unidade e total extraído. Diferenciar notificações, pessoas, eventos de internação e óbitos; não somá-los como pacientes únicos.
4. Não tratar ano de processamento como ano de ocorrência sem confirmar o campo. Não calcular incidência sem população e período compatíveis.
5. Antes da entrega, verificar que o resultado se refere à localidade pedida e separar zero, dado não localizado e base indisponível. Manter a resposta curta com fontes, sem transformar toda consulta em revisão acadêmica.

## Origem e escopo

Adaptação metodológica em PT-BR do ECC 2.2.3, arquivo fornecido pelo usuário, revisão `ef648e01899ba3e8dc6371642deaaf64b4477775`. Fontes:

- `skills/iterative-retrieval/SKILL.md` — SHA-256 `b453b16d3e36174b8487c05ab807d0321a66c2d058812b2ae129d82824183725`
- `skills/verification-loop/SKILL.md` — SHA-256 `503aebee7d414f559c4874600081a40b1e7aea269b58073c5c9660c6641b00a0`

As fontes são registros de procedência; não representam dependências de execução. Os caminhos acima pertencem ao ECC original e não precisam existir neste plugin. Consulte `ECC-NOTICE.md` na raiz para a licença.
