# Guia rápido

## 1. Escolha o pacote pela tarefa

Abra o [catálogo por área](catalogo.md), encontre o objetivo e leia o README do plugin. Escolha só as skills necessárias; não é preciso carregar toda a coleção.

Exemplo: para aprender SQL, usar SQL Mentor. Para analisar um artigo, começar por Pesquisa Científica e depois Artigo Crítico. Para montar flashcards, usar Anki Builder.

## 2. Confira o que o ambiente precisa oferecer

| Tarefa | Requisito |
|---|---|
| Explicar, planejar ou revisar texto fornecido | Agente que leia as instruções |
| Consultar editais, artigos ou preços atuais | Navegação ou dados atuais fornecidos |
| Executar Python, limpar planilhas ou exportar TSV | Runtime e bibliotecas indicados no pacote |
| Gerar imagens e editar artes | Ferramenta de imagem ou editor disponível |
| Criar arquivos de documentos ou apresentações | Ferramentas de geração e renderização |
| Validar DAX ou produzir PBIX | Power BI |
| Usar um servidor MCP incluído | Configuração e dependências do servidor |

O plugin não fornece automaticamente todas essas ferramentas. Se faltar uma dependência, a skill orienta a entregar uma alternativa e informar o que não foi executado.

## 3. Instale pelo mecanismo do seu cliente

Cada diretório `plugins/<nome>` é independente. Para clientes que suportam Agent Skills, usar a pasta `skills/<nome-da-skill>` conforme as instruções oficiais daquele cliente. Para importar um plugin no ChatGPT ou Codex, usar o fluxo de plugins suportado pela versão em uso e o formato exigido por ela.

Um manifesto no GitHub não ativa uma instalação na conta. Os overlays `.codex-plugin/` existem para clientes que os utilizam; não significam que qualquer versão de qualquer cliente foi testada. O formato de plugin Claude Code tem convenções próprias: não presumir que o manifesto OpenAI é intercambiável.

É possível ler um `SKILL.md` como referência de workflow, mesmo sem instalação. Nesse caso, dizer ao agente qual tarefa deve executar com as instruções e fornecer os materiais necessários.

## 4. Faça um pedido concreto

| Pacote | Exemplo de pedido |
|---|---|
| DataLab | “Limpe esta base, preserve códigos de clientes e explique as alterações.” |
| MedQuest | “Faça 9 objetivas e 3 discursivas, com gabarito separado.” |
| Pesquisa Científica | “Extraia métodos e resultados destes artigos com fontes.” |
| PostLab | “Planeje um carrossel de cinco páginas sobre Python e SQL.” |
| Edital Fácil | “Extraia requisitos, prazos e documentos deste edital.” |
| Anki Builder | “Crie cartões deste capítulo e exporte em TSV.” |

Para pesquisa, informe edição, período e local. Para análise de arquivos, forneça o material. Para banco de dados, informe dialeto e esquema.

## 5. Confira a entrega

Verificar fontes, premissas e operações executadas. Código preparado não significa código executado; roteiro não significa arquivo final; arquivo exportado não significa publicado. Os workflows médicos e financeiros são recursos de estudo e análise e precisam preservar incertezas e limites de aplicação.

[Voltar à documentação](README.md)
