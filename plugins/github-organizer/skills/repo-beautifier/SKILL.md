---
name: repo-beautifier
description: Organiza a estrutura de pastas do repositório, adiciona arquivos de comunidade, badges, CI/CD, e ferramentas de qualidade para deixar o projeto com padrão internacional.
---

# Repo Beautifier (Organizador de Repositórios)

Quando esta skill for ativada (ou quando o usuário pedir para organizar/embelezar o repositório), você atuará como um Arquiteto de Software preocupado com a Experiência do Desenvolvedor (DX). 

O seu objetivo é transformar repositórios comuns e bagunçados em projetos de nível profissional internacional (Open Source Quality).

## Passo a Passo de Execução:

### 1. Análise e Limpeza de Estrutura
- Mova arquivos soltos na raiz para pastas organizadas adequadas (ex: `scripts/`, `assets/`, `docs/`, `src/`, `tests/`).
- Renomeie pastas e arquivos para seguir um padrão unificado (ex: `kebab-case` ou `snake_case`), garantindo que as importações sejam corrigidas caso seja necessário.
- Delete logs soltos, arquivos temporários, `.DS_Store` e arquivos inúteis.

### 2. Badges e Documentação (README)
- Adicione **Badges (Shields.io)** no topo do `README.md` refletindo a linguagem principal do projeto, licença, status de CI e dependências.
- Garanta que o README possua seções claras de "Instalação", "Uso" e "Contribuição".

### 3. Comunidade e Templates do GitHub
- Crie a pasta `.github/ISSUE_TEMPLATE/` com templates estruturados (`bug_report.md` e `feature_request.md`).
- Crie o arquivo `.github/PULL_REQUEST_TEMPLATE.md`.
- Garanta a existência do `.gitignore` adequado, `CONTRIBUTING.md` e `LICENSE`.
- Adicione um **`CODE_OF_CONDUCT.md`** usando o padrão internacional (Contributor Covenant) para transmitir profissionalismo e credibilidade.

### 4. Automação e CI/CD (GitHub Actions)
- Crie a pasta `.github/workflows/` e adicione um pipeline de CI básico (ex: `ci.yml`) para testar/buildar o código automaticamente a cada Push e Pull Request.
- Crie um arquivo **`.github/dependabot.yml`** para ativar o robô do GitHub que vai manter as bibliotecas e frameworks sempre atualizados de forma automática.

### 5. Formatação Automática de Código
- Crie o arquivo `.editorconfig` com o padrão de quebra de linhas e indentação.
- Conforme a tecnologia encontrada, configure o **formatador de código ideal** (Prettier para Web, Black para Python, etc.) e adicione um script no gerenciador de pacotes para formatar tudo de uma vez.

### 6. Proteção de Commits (Git Hooks / Husky)
- Adicione regras de **Git Hooks** (usando Husky + lint-staged, pre-commit do Python, ou equivalente). O objetivo é forçar que, antes de qualquer commit ser finalizado, o código seja automaticamente formatado e testado localmente. Código feio ou quebrado não pode entrar no histórico!

### Relatório e Entregáveis Finais
- Faça **commits separados e descritivos** (usando conventional commits) para cada uma das 6 etapas (ex: `ci: add github actions`, `docs: add badges and code of conduct`).
- Ao terminar, mostre ao usuário uma "Árvore de Diretórios" (Tree View) em markdown, exibindo o "Antes" e o "Depois", resumindo a beleza e as melhorias aplicadas no projeto.
