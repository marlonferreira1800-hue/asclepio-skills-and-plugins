---
name: auto-migrator
description: Migra automaticamente bases de código legadas para novas versões de frameworks usando varredura via terminal (grep, sed, replace).
---

# Auto-Migrator (O Atualizador de Frameworks)

Skill avançada para grandes refatorações. Quando solicitada a migração de um projeto (ex: atualizar React, migrar de Python 3.8 para 3.12, trocar pacote HTTP), você atua de forma massiva.

## Diretrizes de Autonomia

1. **Atualização do Manifesto**: Modifique o `package.json`, `requirements.txt` ou `pubspec.yaml` para a nova versão da dependência. Force a instalação, permitindo que a aplicação "quebre".
2. **Coleta de Errors (Blast Radius)**: Rode os testes ou o build do projeto para coletar _TODOS_ os erros de incompatibilidade que a nova versão gerou.
3. **Refatoração Global**:
   - Em vez de alterar os arquivos manualmente um a um, escreva scripts curtos em bash (`find`, `sed`, `grep`), regex ou Python scripts locais (`scratch/`) para substituir chamadas depreciadas por novas chamadas em todos os arquivos de uma vez só.
   - Aplique as substituições em massa.
4. **Ciclo de Ajuste Fino**: Se sobrarem erros residuais pontuais, acesse os arquivos específicos afetados e ajuste a lógica de acordo com a nova documentação (chame sub-agentes de pesquisa se precisar ler a doc do framework novo).
5. **Finalização**: Quando o build voltar a passar limpo na nova versão, faça um grande `git commit` ("refactor: migrate framework to X.Y.Z") e avise o usuário da glória alcançada.
