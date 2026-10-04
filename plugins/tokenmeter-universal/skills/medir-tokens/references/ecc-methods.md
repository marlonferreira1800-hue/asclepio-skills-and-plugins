# Métodos ECC adaptados para tokenmeter-universal

## Arquitetura aplicada

Usar a skill existente como entrada e carregar esta referência somente quando planejar ou revisar a tarefa correspondente. Preservar os scripts, modelos, recursos e integrações do fluxo original. Não ativar hooks, agentes, comandos ou serviços do ECC automaticamente.

Aplicar as etapas desta referência como planejamento e revisão pelo próprio assistente. Não afirmar que especialistas ou agentes independentes foram executados. As instruções do usuário e as regras do ambiente continuam prevalecendo.

## Revisão proporcional

Conferir adequação ao pedido, precisão, fontes necessárias, consistência e formato. Corrigir falhas antes de entregar. Relatar verificações somente quando executadas e distinguir revisão de texto, execução de código, inspeção visual e comportamento no aplicativo.

## Procedimento específico

1. Identificar a semântica da importação antes de somar: evento incremental ou snapshot cumulativo por sessão. Não presumir que todo JSONL contém eventos independentes.
2. Em logs cumulativos do ECC, usar somente o snapshot mais recente por session_id; a soma de todos os snapshots duplica consumo. Conferir timestamp, sessão, modelo e campos de cache. Se o script atual não converter esse formato, preparar uma normalização explícita para o contrato existente antes de importar; não alegar suporte direto novo.
3. Distinguir custo informado pela fonte, custo recalculado com tabela datada e estimativa. Não misturar USD e BRL nem tratar ausência de preço como custo zero.
4. Ao resumir um snapshot por sessão, informar que sua data de atribuição é a do snapshot escolhido; ele não permite reconstruir a distribuição diária das chamadas sem registros mais detalhados.
5. Para otimização, comparar tarefas equivalentes por qualidade, custo e tempo somente quando medidos. Explicar reduções de contexto, cache e tentativas repetidas; não alterar modelos, preços, limites ou integrações automaticamente.

## Origem e escopo

Adaptação metodológica em PT-BR do ECC 2.2.3, arquivo fornecido pelo usuário, revisão `ef648e01899ba3e8dc6371642deaaf64b4477775`. Fontes:

- `skills/cost-tracking/SKILL.md` — SHA-256 `f868207abd550308bc18902ecdfd2c51ad1ea85ba692dbe95cd9c3561da2a8bb`
- `skills/cost-aware-llm-pipeline/SKILL.md` — SHA-256 `2d6c19c2d21a473db8720c4f723f17d265eeec48f84614f0169be2df2fbe28ff`

As fontes são registros de procedência; não representam dependências de execução. Os caminhos acima pertencem ao ECC original e não precisam existir neste plugin. Consulte `ECC-NOTICE.md` na raiz para a licença.
