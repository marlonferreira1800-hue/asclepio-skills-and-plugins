# Decifrando Dados — Newsletter Studio & Gerador Autônomo

Plugin oficial e pipeline de produção da newsletter **Decifrando Dados**, com curadoria e autoria de **Marlon Ferreira**.

- **URL Oficial da Newsletter:** https://www.linkedin.com/newsletters/decifrando-dados-7513791689808064512/
- **Missão:** Desmistificar Ciência de Dados, Machine Learning e Inteligência Artificial, priorizando análises práticas de valor real sobre teorias vazias ou hype.

## Formato Editorial: "The BRIEF"

- **Filosofia / Slogan:** _"Smart people are cooler"_ — sarcástico, espirituoso, pop, ágil, com dados reais mastigados e zero corporatiquês.
- **Público:** Do analista júnior ao C-level/Diretoria técnica.
- **Estrutura Milimétrica:**
  1. _Efeméride/Nostalgia:_ Conexão histórica com o tema do dia.
  2. _Índice Âncora:_ `⚡ O que você vai ver hoje` (escaneável em 5 segundos).
  3. _Matéria de Capa:_ Em caixa alta com destaques (`💡 O número do jogo` e `🎯 Recado para a diretoria`).
  4. _Don't Leave, Just Read:_ Giro de 3 a 4 notícias curtas com emojis temáticos.
  5. _Decifrando na Prática:_ 3 passos técnicos acionáveis.
  6. _A Redação Recomenda & Frase do Dia:_ Fechamento memorável.

## Como Executar o Gerador Autônomo (1 Clique)

Execute `Iniciar Gerador de Newsletter.bat` ou pelo terminal:

```bash
python criar_newsletter.py
```

Cole o link da notícia, caminho de arquivo ou tema desejado e o AGY cuidará de toda a redação, formatação de metadados de SEO, post de divulgação e compilação em PDF.

## Compilação Manual

```bash
python skills/decifrando-dados-newsletter/scripts/build_newsletter.py --input caminho/para/edicao.md --output-dir ./dist --pdf --copy
```

Gera PDF diagramado moderno em alta resolução, HTML interativo com barra de ferramentas e copia o texto pronto para o editor de artigos do LinkedIn.
