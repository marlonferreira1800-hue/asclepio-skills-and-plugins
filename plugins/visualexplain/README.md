# VisualExplain — esqueleto v0.1

Entrada: artigo por URL, PDF, slides, DOCX, texto ou imagem, conforme ferramentas de leitura do agente.
Saída inicial: roteiro JSON + apresentação HTML com etapas animadas.

A skill orienta o agente a ler, explicar e gerar o roteiro; não é um conversor automático autônomo.

## Executar o exemplo

```bash
python3 skills/explicar-visual-animado/scripts/render.py skills/explicar-visual-animado/assets/example.json demo.html
```

Abra demo.html no navegador. Funciona sem servidor e sem dependências externas.

## Expandir

1. Criar extratores para PDF, PPTX, DOCX e OCR, preservando localizadores.
2. Adicionar validação de roteiro e adaptador para um modelo de IA.
3. Criar layouts de comparação, gráficos e diagramas SVG.
4. Adicionar narração e sincronização da linha do tempo.
5. Adicionar exportação MP4 com ferramenta de captura.
6. Se necessário, publicar um serviço MCP e um painel de upload.

Ainda não há servidor MCP, captura de vídeo, voz ou extração integrada. Não inserir chaves no pacote.

## Skills desta ampliação

| Skill                                                                        | Função                      |
| ---------------------------------------------------------------------------- | --------------------------- |
| [`criar-linha-tempo-visual`](skills/criar-linha-tempo-visual/SKILL.md)       | Criar linha do tempo visual |
| [`animar-processo-explicativo`](skills/animar-processo-explicativo/SKILL.md) | Animar processo explicativo |
| [`incluir-quiz-visual`](skills/incluir-quiz-visual/SKILL.md)                 | Incluir perguntas no visual |

## Requisitos e execução

Material fonte, HTML/CSS/JavaScript e navegador para preview; não exige servidor ou conta.

Este pacote fornece instruções reutilizáveis. Não cria conexões, assinaturas, publicação ou execução automática. Os scripts incluídos estão documentados nas skills que os utilizam.

## Exemplos

- Crie uma linha do tempo interativa deste capítulo.
- Anime o trajeto da urina explicado neste material.
- Adicione cinco perguntas com feedback a esta aula visual.
