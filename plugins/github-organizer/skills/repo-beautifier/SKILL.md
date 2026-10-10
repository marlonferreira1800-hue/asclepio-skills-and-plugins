---
name: repo-beautifier
description: Organiza a estrutura de pastas do repositório, adiciona arquivos de comunidade padrão e deixa o projeto limpo, padronizado e "bonito" visualmente.
---

# Repo Beautifier (Organizador de Repositórios)

Quando esta skill for ativada (ou quando o usuário pedir para organizar/embelezar o repositório), você atuará como um arquiteto de software preocupado com a Experiência do Desenvolvedor (DX). 

O seu objetivo é transformar repositórios bagunçados em projetos de padrão internacional.

## Passo a Passo de Execução:

1. **Análise de Estrutura**:
   - Liste todos os arquivos na raiz do repositório.
   - Identifique arquivos soltos que deveriam estar em pastas específicas (ex: scripts avulsos em `scripts/`, imagens em `assets/` ou `docs/`, código-fonte em `src/`, testes em `tests/`).
   - Mova os arquivos para essas pastas criando-as se não existirem (sempre garantindo que os imports internos não quebrem, se for uma linguagem que dependa disso).

2. **Arquivos Comunitários e Templates**:
   - Crie a pasta `.github/ISSUE_TEMPLATE/` com templates de `bug_report.md` e `feature_request.md`.
   - Crie o arquivo `.github/PULL_REQUEST_TEMPLATE.md`.
   - Certifique-se de que existem os arquivos básicos na raiz: `CONTRIBUTING.md`, `LICENSE`, e um `.gitignore` adequado para a linguagem principal do projeto.

3. **Padronização de Nomenclatura**:
   - Avalie se as pastas e arquivos seguem um padrão (ex: `kebab-case` ou `snake_case`). Se houver mistura (ex: `MeuScript.js` junto com `outro-script.js`), sugira a padronização e renomeie, desde que não quebre referências fortes.

4. **Configurações de Editor**:
   - Crie um arquivo `.editorconfig` na raiz do projeto para garantir indentação consistente (ex: 2 ou 4 espaços, utf-8, insert_final_newline).

5. **Limpeza**:
   - Identifique arquivos temporários, logs antigos (`.log`), backups ou arquivos inúteis (como `.DS_Store`) e os delete.

6. **Relatório Visual**:
   - Ao final do processo, exiba ao usuário uma "Árvore de Diretórios" (usando markdown) mostrando o "Antes" e o "Depois" do repositório, para destacar a organização.

Sempre aplique essas regras com o máximo de autonomia, documentando em commits organizados as mudanças estruturais que fizer!
