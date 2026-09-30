---
name: linkedin-conteudo-diario
description: >-
  Cria e agenda lotes diários de posts educativos para LinkedIn sobre dados,
  Python, IA, machine learning, SQL, Excel e temas relacionados. Use quando o
  usuário pedir posts para LinkedIn, um lote diário, conteúdo com imagens ou
  publicação distribuída durante o dia. O padrão é cinco posts com imagens,
  horários de Brasília e uma aprovação explícita do lote antes do agendamento.
---

# LinkedIn Conteúdo Diário

## Overview

Prepare lotes profissionais para LinkedIn com textos educativos, imagens
originais, validação local e agendamento nativo na plataforma. O fluxo padrão
produz cinco posts por dia nos horários 08:00, 10:30, 13:00, 16:00 e 19:00 em
`America/Sao_Paulo`.

Esta skill não armazena credenciais, não usa APIs não oficiais do LinkedIn e não
publica sem aprovação explícita do lote atual.

## Dependencies

- `imagegen`: gerar uma imagem original para cada post, seguindo a identidade
  visual descrita em `assets/README.md`.
- `computer-use:computer-use`: operar o LinkedIn na sessão autenticada do
  usuário, anexar as imagens, configurar horários e confirmar o agendamento.
- `uv`: executar `scripts/linkedin_queue.py` de forma consistente.

Leia completamente a skill de cada dependência antes de usá-la. A política de
confirmação do controle do computador continua valendo: solicite aprovação
imediatamente antes de iniciar a sequência que agenda o lote.

## Quick Start

Pedido típico:

> Crie meu lote diário do LinkedIn sobre Python, SQL, Excel, IA e machine
> learning. Mostre tudo para aprovação antes de agendar.

Comportamento padrão:

1. preparar cinco posts e cinco imagens;
2. validar o lote;
3. apresentar textos, imagens e horários;
4. pedir uma única aprovação explícita;
5. agendar os cinco posts no LinkedIn na mesma sequência de execução;
6. registrar os identificadores e resultados.

## Utility Scripts

Execute sempre com `uv run`.

### Criar a fila

```powershell
uv run scripts/linkedin_queue.py plan `
  --date 2026-10-01 `
  --timezone America/Sao_Paulo `
  --quantity 5 `
  --times 08:00,10:30,13:00,16:00,19:00 `
  --topics "Python,SQL,Excel,IA,Machine Learning" `
  --assets-dir linkedin-posts/2026-10-01 `
  --output linkedin-posts/2026-10-01/queue.json
```

### Validar textos e imagens

```powershell
uv run scripts/linkedin_queue.py validate `
  --queue linkedin-posts/2026-10-01/queue.json `
  --output linkedin-posts/2026-10-01/validation.json
```

Não abra o LinkedIn se `valid` for `false`.

### Consultar o estado

```powershell
uv run scripts/linkedin_queue.py status `
  --queue linkedin-posts/2026-10-01/queue.json `
  --output linkedin-posts/2026-10-01/status.json
```

### Registrar um agendamento

```powershell
uv run scripts/linkedin_queue.py record `
  --queue linkedin-posts/2026-10-01/queue.json `
  --item-id post-01 `
  --status scheduled `
  --external-id urn:li:activity:EXEMPLO `
  --url https://www.linkedin.com/feed/update/urn:li:activity:EXEMPLO/ `
  --output linkedin-posts/2026-10-01/queue.json
```

## Workflow

### 1. Definir o lote

- Use cinco itens salvo quando o usuário informar outra quantidade.
- Se ele fornecer menos temas que itens, complemente com uma rotação entre
  Python, Pandas, SQL, Excel, IA, machine learning, qualidade de dados,
  visualização, dashboards, portfólio e carreira.
- Consulte lotes recentes no diretório `linkedin-posts` para evitar repetição
  de temas, ganchos, exemplos e perguntas.
- Gere a fila com o utilitário antes de criar o conteúdo.
- Se um horário do dia já passou, não publique nem retroaja silenciosamente:
  proponha usar o próximo dia ou peça uma decisão.

### 2. Escrever os posts

- Siga `references/editorial-guide.md`.
- Produza conteúdo correto, educativo, profissional e acessível a iniciantes.
- Cada post deve ter gancho, explicação prática, pergunta de engajamento e de
  três a cinco hashtags relevantes.
- Não invente experiência pessoal, emprego, projeto concluído ou resultados do
  usuário.
- Salve cada texto em `posts/NN.md`, conforme os caminhos da fila.

### 3. Gerar as imagens

- Use `imagegen`, uma chamada por imagem.
- Gere no máximo duas imagens simultaneamente.
- Use a identidade azul, ciano e laranja descrita em `assets/README.md`.
- Evite logotipos, marcas d'água, texto ilegível, interfaces copiadas e mãos
  deformadas.
- Copie cada arquivo final para o caminho registrado na fila.
- Em caso de falha, tente novamente uma vez com uma instrução mais simples.

### 4. Validar e apresentar

- Execute `validate` e corrija todos os erros antes de prosseguir.
- Mostre ao usuário os cinco textos, as cinco imagens e os horários.
- Informe claramente que a próxima ação criará publicações agendadas em seu
  nome e visíveis a terceiros.
- Peça uma aprovação explícita do lote atual.

### 5. Agendar no LinkedIn

- Somente após a aprovação, leia e siga `computer-use:computer-use`.
- Use a sessão já autenticada do usuário. Nunca solicite ou manipule senha.
- Para cada item: abrir o compositor, inserir o texto, anexar a imagem, escolher
  o horário da fila e confirmar o agendamento.
- Faça a sequência inteira imediatamente após a aprovação, evitando novas
  confirmações redundantes quando destino, conteúdo e horários não mudarem.
- Após cada agendamento, verifique uma confirmação autoritativa da plataforma e
  registre o resultado com `record`.

### 6. Recuperar de falhas

- Falha de geração: repetir uma vez; depois marcar o item como `failed`.
- Falha do LinkedIn: reobservar a página e repetir uma vez somente se o estado
  anterior for conhecido.
- Estado incerto: consultar publicações agendadas antes de qualquer repetição.
- CAPTCHA, autenticação, barreira de segurança ou limite explícito: parar e
  entregar o controle ao usuário.
- Preserve itens já agendados e informe exatamente de qual item retomar.

## Rate Limiting

Não há API nova nesta skill. Limites são operacionais:

- no máximo duas gerações de imagem simultâneas;
- cinco posts no lote padrão;
- horários distribuídos ao longo do dia;
- qualquer limite exibido pelo LinkedIn encerra a tentativa automática.

## Common Mistakes

- Publicar os cinco posts imediatamente em vez de usar os horários da fila.
- Agendar sem aprovação explícita do lote atual.
- Repetir uma publicação quando o resultado anterior está incerto.
- Reutilizar a mesma imagem, gancho ou pergunta em posts consecutivos.
- Criar fatos pessoais ou profissionais não fornecidos pelo usuário.

