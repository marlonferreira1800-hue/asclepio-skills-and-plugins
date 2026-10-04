# MedQuest — Medicina por Questões

Tutor de aprendizagem ativa para estudantes de Medicina e médicos em preparação para provas (Residência Médica, Revalida, ENAMED e graduação).

## Visão Geral

O **MedQuest** conduz sessões interativas de estudo orientadas por questões e raciocínio clínico deliberado, sem antecipar o gabarito. Ele prioriza a compreensão fisiopatológica, o diagnóstico diferencial e a retenção de longo prazo.

## Habilidade Incluída

- **`questoes-medicina`**:
  - **Questões Objetivas (A–E)**: Enunciados contextualizados com alternativas desafiadoras; espera a resposta antes de fornecer gabarito.
  - **Correção Comentada**: Explica a alternativa correta e justifica o erro dos distratores clinicamente relevantes.
  - **Casos Clínicos Progressivos**: Raciocínio por etapas (QP → HDA → Exame Físico → Exames Complementares → Diagnóstico/Conduta).
  - **Método Cognitus**: Explicação por mecanismos, analogias didáticas e calibragem da dificuldade conforme o desempenho.
  - **Revisão Ativa e Flashcards**: Identifica pontos frágeis na sessão e gera flashcards de fixação de alto rendimento.
  - **Simulados no estilo ENAMED**: Produção de simulados autorais balanceados para prática intensiva.

## Como Usar

Exemplos de prompts para iniciar:

```text
"Comece um treino de Medicina com questões objetivas sobre Cardiologia."
"Crie um caso clínico de Pediatria e espere minha resposta antes de corrigir."
"Revise meus erros da sessão e faça novas questões focadas nas minhas dificuldades."
"Crie um simulado de 5 questões no estilo ENAMED com gabarito comentado no final."
```

## Skills desta ampliação

| Skill | Função |
|---|---|
| [`classificar-questoes-medicas`](skills/classificar-questoes-medicas/SKILL.md) | Classificar questões médicas |
| [`analisar-erros-estudo`](skills/analisar-erros-estudo/SKILL.md) | Analisar erros de estudo |
| [`criar-prova-equivalente`](skills/criar-prova-equivalente/SKILL.md) | Criar prova equivalente |

## Requisitos e execução

Questões e gabarito; fontes médicas atuais para conteúdo clínico. Uso educacional.

Este pacote fornece instruções reutilizáveis. Não cria conexões, assinaturas, publicação ou execução automática. Os scripts incluídos estão documentados nas skills que os utilizam.

## Exemplos

- Organize estas questões de imunologia por tema.
- Analise meus erros desta prova e monte uma revisão por tema.
- Faça outra prova com 9 objetivas e 3 discursivas sobre os mesmos temas.
