# 🎂 Receita de Bolo Oficial: Newsletter 'Decifrando Dados'

Este documento define o pipeline milimétrico, obrigatório e padronizado para produzir, diagramar e publicar qualquer edição da newsletter oficial **Decifrando Dados** (por **Marlon Ferreira** no LinkedIn).

---

## 🥣 1. Ingredientes Obrigatórios

Toda nova edição precisa partir de 4 ingredientes essenciais:

1. **Fato / Link Central:** Notícia factual ou avanço técnico do ecossistema de dados/IA.
2. **Formato Editorial Exclusivo:** O padrão **The BRIEF** (_"Smart people are cooler"_ — sarcástico, ágil, pop e sem corporatiquês).
3. **Métrica de Impacto:** Um número real mastigado (dólares, %, latência, benchmarks).
4. **Metadados Completos:** O bloco de SEO e Divulgação no LinkedIn.

---

## ⚙️ 2. Bloco Obrigatório de Metadados & Distribuição

Toda edição gerada deve conter obrigatoriamente no topo da entrega (e no cabeçalho do arquivo gerado para o LinkedIn) a estrutura milimétrica abaixo:

```text
======================================================================
DECIFRANDO DADOS - EDIÇÃO XX
======================================================================

⚙️ Metadados de SEO para o LinkedIn
Título SEO: [Título direto, focado na palavra-chave principal | Decifrando Dados]

Descrição SEO: [Resumo persuasivo com 140 a 160 caracteres contendo palavras-chave para indexação no Google e no LinkedIn]

* Copie estes dados manualmente para a área de SEO do LinkedIn. O botão azul copiará apenas o texto do artigo.

----------------------------------------------------------------------
📢 Post de Divulgação ("Conte para sua rede..."):
----------------------------------------------------------------------
[Gancho provocativo e forte nas primeiras duas linhas que capture a atenção no feed]

[Breve contexto em 1-2 parágrafos apresentando a tese central da edição da Decifrando Dados]

[Pergunta aberta estimulando o engajamento e comentários da comunidade]

#dados #analytics #carreira #ia #sql
======================================================================
```

### 💡 Por que este bloco é obrigatório?

- **Indexação (SEO):** Se não preenchido nas configurações do LinkedIn, o Google e o buscador do LinkedIn puxam trechos aleatórios do texto.
- **Aviso do Botão Azul:** Avisa ao autor que o botão de 1 clique copia **apenas o conteúdo do artigo**, permitindo colar com `Ctrl + V` sem sujar o artigo com os metadados.
- **Tração no Feed:** 90%+ dos leitores entram pelo feed na caixa _"Conte para sua rede..."_. O post já sai pronto, sem exigir redação na hora.

---

## 🧑‍🍳 3. Modo de Preparo (Estrutura do Artigo: "The BRIEF")

O corpo do Markdown segue estritamente as camadas editoriais:

1. **Frontmatter YAML:**
   ```yaml
   ---
   titulo: "..."
   subtitulo: "..."
   edicao: "XX"
   data: "DD/MM/AAAA"
   tempo_leitura: "X"
   seo_titulo: "..."
   seo_descricao: "..."
   post_divulgacao: |
     ...
   ---
   ```
2. **Efeméride/Nostalgia:** "Há X anos na tecnologia..." abrindo com curiosidade histórica conectada à pauta.
3. **Índice Âncora:** "⚡ O que você vai ver hoje" (sumário escaneável em 5 segundos com ganchos provocativos e emojis).
4. **Matéria de Capa:**
   - Categoria em caixa alta (ex: `PODER & NEGÓCIOS ÁGEIS`, `ENGENHARIA & DADOS`).
   - Manchete provocativa.
   - Referências de cultura pop e dados reais mastigados.
   - Métrica em destaque (`> 💡 **O número do jogo:** ...`).
   - Provocação direta para a liderança (`> 🎯 **Recado para a diretoria:** ...`).
5. **Don't Leave, Just Read:** Giro expresso de 3 a 4 notícias curtas com emojis temáticos em no máximo 2 parágrafos ágeis cada.
6. **Decifrando na Prática:** 3 passos técnicos acionáveis para o leitor aplicar na semana.
7. **A Redação Recomenda & Frase do Dia:** Indicação prática de repositório/ferramenta e citação memorável/irônica de fechamento.

---

## 🚫 4. Filtro Anticlichê de IA

- **Termos Banidos:** É expressamente proibido usar _"mergulhar"_, _"revolucionário"_, _"crucial"_, _"panorama"_, _"testamento"_, _"no fim das contas"_.
- **Pontuação:** Proibido uso excessivo de travessões (`—`).
- **Estilo:** Priorizar exemplos concretos, código conciso e métricas reais sobre discursos genéricos.

---

## ♨️ 5. Forno (Compilação Automática)

Toda edição é compilada rodando o comando utilitário:

```powershell
python build_newsletter.py --input caminho/para/edicao.md --output-dir "C:\Users\marlo\Downloads\dados25" --pdf --copy
```

**O que o script entrega:**

1. **Arquivo HTML com Toolbar de 1 Clique:**
   - Botão azul destacado no topo: **"📋 Copiar Texto Formatado e Abrir LinkedIn"**. Ao clicar, o script copia o conteúdo formatado em Rich Text direto para o clipboard e abre o LinkedIn em nova aba.
   - Caixa de Metadados de SEO e Post de Divulgação logo abaixo do botão para cópia rápida.
   - Totalmente invisível na impressão (`@media print`), preservando o layout limpo.
2. **Arquivo PDF Editorial:** Diagramado em alta resolução compilado pelo Microsoft Edge headless (em `C:\Users\marlo\Downloads\dados25`).
3. **Arquivo de Texto Completo:** `_artigo_linkedin.txt` com o bloco estruturado de SEO, Post de Divulgação e Artigo formatado.
4. **Cópia Instantânea:** Conteúdo do artigo já injetado na Área de Transferência do Windows (`Ctrl + V`).

---

## 🍽️ 6. Servir (Publicação em 30 Segundos no LinkedIn)

1. Abra o arquivo `.html` gerado no seu navegador.
2. Copie manualmente o **Título SEO** e a **Descrição SEO** da caixa cinza.
3. Clique no botão azul: **"📋 Copiar Texto Formatado e Abrir LinkedIn"**.
   - O texto formatado com títulos e negritos é copiado automaticamente.
   - Uma nova aba do LinkedIn abre imediatamente.
4. Cole os dados de SEO na engrenagem de configurações do artigo do LinkedIn.
5. No corpo do editor de artigo, aperte **Ctrl + V**.
6. Clique em **Avançar** e cole o texto do **Post de Divulgação** na caixa _"Conte para sua rede..."_.
7. Clique em **Publicar**.
