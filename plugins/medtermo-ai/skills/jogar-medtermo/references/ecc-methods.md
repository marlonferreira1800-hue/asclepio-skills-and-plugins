# Métodos ECC adaptados para medtermo-ai

## Arquitetura aplicada

Usar a skill existente como entrada e carregar esta referência somente quando planejar ou revisar a tarefa correspondente. Preservar os scripts, modelos, recursos e integrações do fluxo original. Não ativar hooks, agentes, comandos ou serviços do ECC automaticamente.

Aplicar as etapas desta referência como planejamento e revisão pelo próprio assistente. Não afirmar que especialistas ou agentes independentes foram executados. As instruções do usuário e as regras do ambiente continuam prevalecendo.

## Revisão proporcional

Conferir adequação ao pedido, precisão, fontes necessárias, consistência e formato. Corrigir falhas antes de entregar. Relatar verificações somente quando executadas e distinguir revisão de texto, execução de código, inspeção visual e comportamento no aplicativo.

## Procedimento específico

1. Adaptar a avaliação por tarefas do ECC ao jogo: definir cenário e critérios de comportamento antes de avaliar; não instalar a ferramenta de comparação de agentes.
2. Conferir internamente que diagnóstico, sinônimos e pistas permanecem coerentes durante a rodada. Não expor diagnóstico, checklist ou referência que revele a resposta antes do desfecho.
3. Avaliar regras de estado: exatamente cinco palpites errados possíveis; pergunta sobre regras não gasta tentativa; palpite ambíguo pede esclarecimento; nenhum contador negativo.
4. Após acerto ou esgotamento, explicar as pistas principais e a diferença em relação a um diagnóstico plausível. Manter a verificação de fonte atual para condutas que o fluxo original exigir.
5. Separar revisão do caso fictício de orientação para um relato pessoal real. Verificar que a revisão não acrescenta achados inexistentes para justificar retroativamente o diagnóstico.

## Origem e escopo

Adaptação metodológica em PT-BR do ECC 2.2.3, arquivo fornecido pelo usuário, revisão `ef648e01899ba3e8dc6371642deaaf64b4477775`. Fontes:

- `skills/agent-eval/SKILL.md` — SHA-256 `57fa683e356b6f5612bc6d7dc101ae39c126e6edf9a48f4ec53afea3e80d7e5d`
- `skills/verification-loop/SKILL.md` — SHA-256 `503aebee7d414f559c4874600081a40b1e7aea269b58073c5c9660c6641b00a0`

As fontes são registros de procedência; não representam dependências de execução. Os caminhos acima pertencem ao ECC original e não precisam existir neste plugin. Consulte `ECC-NOTICE.md` na raiz para a licença.
