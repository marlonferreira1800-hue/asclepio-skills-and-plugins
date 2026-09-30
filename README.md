# Asclépio — Skills & Plugins para Agentes de IA

<p align="center">
  <strong>Ecossistema modular de plugins e habilidades (skills) para tutoria médica ativa, raciocínio clínico deliberado, síntese visual de estudos e produtividade educacional.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Vers%C3%A3o-1.0.0-blue.svg" alt="Versão 1.0.0">
  <img src="https://img.shields.io/badge/Plugins-6_Integrados-success.svg" alt="6 Plugins">
  <img src="https://img.shields.io/badge/Compatibilidade-Codex%20%7C%20ChatGPT%20%7C%20Claude%20%7C%20Antigravity-orange.svg" alt="Compatibilidade">
  <img src="https://img.shields.io/badge/Licen%C3%A7a-MIT-green.svg" alt="Licença MIT">
</p>

---

## 🏛️ Sobre o Projeto

O **Asclépio** (em referência à divindade grega da medicina e da cura) é uma coleção estruturada de plugins e skills para modelos de linguagem e agentes autônomos de IA. 

O repositório reúne ferramentas especializadas que transformam LLMs em tutores ativos, avaliadores clínicos diagnósticos, desenhistas de resumos visuais de alta retenção e facilitadores de produção de conteúdo educativo.

---

## 📦 Catálogo de Plugins e Habilidades

| Plugin | Habilidade (`skill`) | Categoria | Descrição Principal |
|---|---|---|---|
| [**MedQuest**](plugins/medquest) | `questoes-medicina` | Educação Médica | Treino ativo por questões objetivas, casos clínicos progressivos, correção comentada e simulados estilo ENAMED. |
| [**MedTermo AI**](plugins/medtermo-ai) | `jogar-medtermo` | Raciocínio Clínico / Jogo | Jogo de adivinhação diagnóstica em até 5 tentativas com liberação gradual de pistas e revisão de alto rendimento. |
| [**Cognitus**](plugins/cognitus) | `aprendizagem-ativa` | Tutoria Cognitiva | Aprendizagem ativa baseada em método socrático, técnica de Feynman, diagramas Mermaid e flashcards Anki. |
| [**Mentor de Estudos**](plugins/mentor-de-estudos) | `tutoria-de-estudos` | Planejamento de Estudos | Mentoria personalizada para estruturação de cronogramas, revisão sistemática e acompanhamento de metas. |
| [**Resumo Visual Manuscrito**](plugins/resumo-visual-manuscrito) | `criar-resumo-visual` | Design & Síntese Visual | Transformação de apostilas e temas densos em folhas de estudo ilustradas, caligrafadas e com caixas de prova. |
| [**LinkedIn Conteúdo Diário**](plugins/linkedin-conteudo-diario) | `linkedin-conteudo-diario` | Produtividade | Preparação e organização em lotes de posts educativos com imagens, validação e fila local de agendamento. |

---

## 🔍 Detalhamento dos Plugins

### 🩺 1. MedQuest — Medicina por Questões
- **Objetivo**: Conduzir o estudante por um treino deliberado onde o gabarito nunca é revelado de imediato.
- **Destaques**:
  - Questões objetivas (A–E) com análise crítica dos distratores.
  - Casos clínicos com liberação progressiva da vinheta (Queixa → HDA → Exame Físico → Exames → Conduta).
  - Geração automatizada de flashcards de fixação Anki após a demonstração de domínio conceitual.
  - Simulados autorais balanceados no padrão ENAMED e bancas de Residência Médica.

### 🎯 2. MedTermo AI — Desafio Diagnóstico
- **Objetivo**: Treinar o raciocínio dedutivo rápido diante de vinhetas clínicas reais.
- **Mecânica**:
  - O usuário tem **5 tentativas** para cravar o diagnóstico principal.
  - A cada palpite incorreto, o assistente desconta uma tentativa e libera uma pista hierarquizada (Exame Físico → Laboratório → Imagem/ECG → Pista de Prova/Patognomônica).
  - Ao final, apresenta uma revisão concisa: diagnóstico correto, pistas essenciais de prova e conduta terapêutica imediata.

### 🧠 3. Cognitus — Aprendizagem Ativa
- **Objetivo**: Combater a ilusão de competência provocada pela leitura passiva.
- **Metodologia**:
  - Aplicação do Método Socrático: estimula o raciocínio antes de antecipar conclusões.
  - Técnica de Feynman para simplificação e analogias com limites definidos.
  - Diagramação visual em tempo real com sintaxe Mermaid.
  - Síntese de flashcards direcionados para repetição espaçada.

### 📚 4. Mentor de Estudos
- **Objetivo**: Planejamento estratégico de rotina de estudos acadêmicos e para concursos.
- **Recursos**:
  - Diagnóstico de tempo disponível, metas e nível prévio do estudante.
  - Criação de planos de estudos modulares e intercalados.
  - Monitoramento contínuo de retenção e adaptação dinâmica do cronograma.

### 🎨 5. Resumo Visual Manuscrito
- **Objetivo**: Síntese de alta performance no formato de fichamento ilustrado.
- **Elementos Visuais**:
  - Estruturação em 5 a 9 blocos didáticos prioritários.
  - Seção fixa `🧠 MEMORIZE PARA A PROVA` com dados de alto rendimento.
  - Seção de alerta `⚠️ NÃO CONFUNDA` para diferenciação de pegadinhas frequentes.
  - Geração de prompts otimizados para renderização de cadernos e folhas visuais.

### 🚀 6. LinkedIn Conteúdo Diário
- **Objetivo**: Automação e consistência na publicação de posts técnicos e acadêmicos.
- **Capacidades**:
  - Script local em Python (`linkedin_queue.py`) para gestão de fila e validação sem chamadas externas inseguras.
  - Preparação de lotes de 5 posts com imagens associadas e horários ajustados para o fuso de Brasília.
  - Garantia de governança: nenhuma publicação ocorre sem aprovação prévia explícita.

---

## 🗂️ Estrutura do Repositório

```text
asclepio-skills-and-plugins/
├── .gitignore
├── LICENSE
├── README.md
├── plugins-index.json
└── plugins/
    ├── cognitus/
    │   ├── .codex-plugin/
    │   │   └── plugin.json
    │   ├── plugin.json
    │   ├── README.md
    │   └── skills/
    │       └── aprendizagem-ativa/
    │           └── SKILL.md
    ├── linkedin-conteudo-diario/
    │   ├── .codex-plugin/
    │   │   └── plugin.json
    │   ├── assets/
    │   │   └── icon.svg
    │   ├── plugin.json
    │   ├── README.md
    │   └── skills/
    │       └── linkedin-conteudo-diario/
    │           ├── assets/
    │           ├── references/
    │           ├── scripts/
    │           │   └── linkedin_queue.py
    │           └── SKILL.md
    ├── medquest/
    │   ├── .codex-plugin/
    │   │   └── plugin.json
    │   ├── plugin.json
    │   ├── README.md
    │   └── skills/
    │       └── questoes-medicina/
    │           └── SKILL.md
    ├── medtermo-ai/
    │   ├── .codex-plugin/
    │   │   └── plugin.json
    │   ├── plugin.json
    │   ├── README.md
    │   └── skills/
    │       └── jogar-medtermo/
    │           └── SKILL.md
    ├── mentor-de-estudos/
    │   ├── .codex-plugin/
    │   │   └── plugin.json
    │   ├── plugin.json
    │   ├── README.md
    │   └── skills/
    │       └── tutoria-de-estudos/
    │           └── SKILL.md
    └── resumo-visual-manuscrito/
        ├── .codex-plugin/
        │   └── plugin.json
        ├── plugin.json
        ├── README.md
        └── skills/
            └── criar-resumo-visual/
                └── SKILL.md
```

---

## 💻 Instalação e Utilização

### No OpenAI Codex / ChatGPT
1. Cada plugin possui o arquivo de manifesto `plugin.json` e a pasta `.codex-plugin/plugin.json` compatíveis com o padrão do Codex e do schema `agent-plugins.org`.
2. Para instalar um plugin específico, aponte o carregamento para a pasta do plugin desejado em `plugins/<nome-do-plugin>`.

### No Antigravity IDE / Claude Code
1. Copie as pastas localizadas dentro de `plugins/<plugin>/skills/<skill-name>` para o diretório de skills do seu workspace (`.agents/skills/`) ou para o root global (`~/.gemini/config/skills/`).
2. Os arquivos `SKILL.md` incluem frontmatter YAML completo com metadados de ativação (`name` e `description`).

---

## 🔒 Segurança e Boas Práticas

- **Sem Credenciais Embutidas**: Nenhum arquivo deste repositório armazena chaves de API, senhas ou tokens de acesso.
- **Rigor Científico & Educacional**: Os plugins de medicina são orientados a recursos educacionais, incentivando o raciocínio independente e a consulta de fontes primárias e diretrizes reconhecidas.
- **Execução Local**: Todos os utilitários (como o gerenciador de filas em Python) operam exclusivamente no sistema de arquivos local.

---

## 📄 Licença

Distribuído sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">
  Desenvolvido por <strong>Marlon Ferreira</strong>
</p>
