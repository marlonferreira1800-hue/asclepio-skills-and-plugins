---
name: git-conflict-resolver
description: Lê arquivos em conflito no Git, compreende as intenções de ambas as branches e realiza o merge do código automaticamente pelo terminal.
---

# Git Conflict Auto-Resolver (O Mestre dos Merges)

Quando o usuário relatar que há um merge conflict, você assumirá a responsabilidade de resolvê-lo ponta a ponta sem fazer perguntas.

## Diretrizes de Autonomia

1. **Varredura**: Execute `git status` para listar os arquivos "both modified" (com conflitos).
2. **Análise Semântica**: Em cada arquivo, leia os blocos `<<<<<<< HEAD` até `>>>>>>> branch`. Compreenda o que a _branch atual_ estava tentando fazer e o que a _branch de origem_ modificou.
3. **Resolução Inteligente**:
   - Não apenas aceite o lado A ou B cegamente. Faça o merge manual das lógicas (ex: se A adicionou um botão e B mudou a cor do fundo da tela, aplique ambas as mudanças).
   - Reescreva o bloco removendo as marcações de conflito do Git.
4. **Validação (Self-Check)**: Verifique se o código resultante tem sintaxe válida e não quebrou a estrutura do arquivo. Rode linters ou testes, se existirem e forem rápidos.
5. **Finalização**: Rode `git add <arquivo_resolvido>` para todos eles e, em seguida, faça o `git commit -m "chore: auto-resolve merge conflicts"`. Avise o usuário que o merge foi finalizado com sucesso.
