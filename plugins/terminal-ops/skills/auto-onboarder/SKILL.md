---
name: auto-onboarder
description: Configura automaticamente projetos recém-clonados do zero. Instala dependências, cria variáveis de ambiente e sobe bancos de dados via terminal.
---

# Auto-Onboarder (Configurador de Ambientes)

Quando esta skill for ativada na raiz de um projeto recém-clonado, seu objetivo é colocar o ambiente de desenvolvimento para rodar **sem intervenção humana**.

## Diretrizes de Autonomia

1. **Descoberta**: Leia imediatamente o `README.md`, `package.json`, `requirements.txt`, `docker-compose.yml` ou similares para descobrir a stack do projeto.
2. **Ambiente**:
   - Se existir um arquivo `.env.example`, copie-o para `.env` e preencha chaves básicas locais (como senhas default de banco de dados).
   - Verifique a versão da linguagem necessária e instale as dependências pelo terminal (ex: `npm install`, `pip install -r requirements.txt`).
3. **Infraestrutura**: Se houver um `docker-compose.yml`, rode `docker-compose up -d` para subir bancos de dados ou serviços em background.
4. **Resolução de Problemas Base**: Se a instalação de um pacote falhar por falta de dependência no SO, tente resolver ou adapte.
5. **Teste de Inicialização**: Inicie o servidor de desenvolvimento (ex: `npm run dev`, `python manage.py runserver`) e verifique os logs para garantir que não crashou.
6. **Entrega Final**: Quando o servidor estiver de pé, notifique o usuário informando em qual porta (`localhost:PORTA`) o projeto está rodando e quais serviços foram configurados.
