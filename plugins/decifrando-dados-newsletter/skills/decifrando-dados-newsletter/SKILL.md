---
name: decifrando-dados-newsletter
description: >-
  Cria e compila edições para a newsletter 'Decifrando Dados' de Marlon Ferreira sobre
  Ciência de Dados, Machine Learning e Inteligência Artificial. Produz PDF diagramado
  profissional com tipografia moderna e exporta o texto formatado pronto para copiar e colar
  diretamente no editor de Artigos do LinkedIn.
---

# Decifrando Dados: Newsletter Studio

Este skill orienta a produção de ponta a ponta das edições da newsletter **Decifrando Dados** (por Marlon Ferreira no LinkedIn: https://www.linkedin.com/newsletters/decifrando-dados-7513791689808064512/).

## Capacidades

1. **Redação Editorial:** Cria edições equilibrando Ciência de Dados, Machine Learning e Inteligência Artificial, sempre com análises práticas e tendências atuais.
2. **Exportação em PDF:** Compila o conteúdo em um documento PDF diagramado com padrão editorial visualmente impecável.
3. **Formatação para Artigo do LinkedIn:** Gera arquivo com hierarquia correta de títulos e espaçamentos para publicação imediata no publicador de Artigos da newsletter do LinkedIn.
4. **Cópia Instantânea:** Envia o artigo formatado para a Área de Transferência (Clipboard do Windows) para colar com `Ctrl + V`.

## Estrutura Padrão de uma Edição

- **Título do Artigo:** Curto, provocativo e focado em benefício ou reflexão prática.
- **Subtítulo:** 1 frase esclarecedora sobre o tema central da edição.
- **Introdução:** Gancho com o momento atual do mercado e saudação aos leitores da _Decifrando Dados_.
- **Pilar 1 (Ciência de Dados):** Análise prática de dados no negócio (SQL, pipelines, métricas que importam).
- **Pilar 2 (Machine Learning):** Aplicação real de modelos, eficácia, qualidade de dados e trade-offs técnicos.
- **Pilar 3 (Inteligência Artificial):** Tendência de mercado (automação, agentes, novas ferramentas) e impacto no dia a dia.
- **Decifrando na Prática:** 3 passos acionáveis para o leitor aplicar na semana.
- **Fechamento e CTA:** Pergunta para comentários e convite à inscrição.

## Como Compilar Edições

Utilize o script utilitário `build_newsletter.py`:

```powershell
python scripts/build_newsletter.py --input caminho/para/edicao.md --output-dir ./dist --pdf --copy
```

### Argumentos Úteis:

- `--input` / `-i`: Caminho do arquivo Markdown da edição.
- `--output-dir` / `-o`: Pasta de destino dos arquivos (HTML, PDF e Artigo).
- `--pdf`: Dispara a compilação do PDF profissional via Edge headless.
- `--copy`: Copia o conteúdo do artigo automaticamente para a Área de Transferência do Windows.

## Guia Rápido de Publicação no LinkedIn

1. Abra a sua newsletter no LinkedIn: [Decifrando Dados](https://www.linkedin.com/newsletters/decifrando-dados-7513791689808064512/).
2. Clique em **Escrever artigo** / **Criar edição**.
3. Selecione o texto gerado no arquivo `_artigo_linkedin.txt` (ou dê `Ctrl + V` se usou o argumento `--copy`).
4. Adicione uma imagem de capa (recomendada proporção horizontal 16:9 ou 1200x644px).
5. Clique em **Avançar**, cole a chamada para o feed sugerida no rodapé do arquivo e publique.
