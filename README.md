# Asclépio — Skills & Plugins para Agentes de IA

<p align="center">
  <strong>Ecossistema modular de plugins e habilidades para aprendizagem, produtividade e pesquisa prática em diferentes áreas.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Plugins-14_Integrados-success.svg" alt="14 plugins">
  <img src="https://img.shields.io/badge/Compatibilidade-Codex%20%7C%20ChatGPT%20%7C%20Claude%20%7C%20Antigravity-orange.svg" alt="Compatibilidade">
  <img src="https://img.shields.io/badge/Licen%C3%A7a-MIT-green.svg" alt="Licença MIT">
</p>

---

## Sobre o projeto

O **Asclépio** reúne plugins e skills portáteis para estudo, pesquisa, produtividade e criação. Cada plugin tem um manifesto, uma skill com instruções de uso e um README próprio. Os plugins de instruções usam as ferramentas disponíveis no assistente; não alegam possuir APIs ou integrações que não estejam configuradas.

## Catálogo

| Plugin | Skill | Categoria | Função |
|---|---|---|---|
| [Cognitus](plugins/cognitus) | `aprendizagem-ativa` | Educação | Tutoria ativa com método socrático, Feynman e flashcards. |
| [Dados de Saúde Brasil](plugins/dados-saude-brasil) | `consulta-dados-doencas` | Saúde pública | Pesquisa dados agregados de doenças em fontes oficiais do SUS. |
| [MedQuest](plugins/medquest) | `questoes-medicina` | Educação médica | Treino de Medicina com questões e casos progressivos. |
| [MedTermo AI](plugins/medtermo-ai) | `jogar-medtermo` | Educação médica | Jogo de adivinhação diagnóstica com pistas graduais. |
| [Mentor de Estudos](plugins/mentor-de-estudos) | `tutoria-de-estudos` | Educação | Planejamento e acompanhamento de estudos. |
| [Resumo Visual Manuscrito](plugins/resumo-visual-manuscrito) | `criar-resumo-visual` | Educação e design | Converte temas em folhas visuais de revisão. |
| [LinkedIn Conteúdo Diário](plugins/linkedin-conteudo-diario) | `linkedin-conteudo-diario` | Produtividade | Prepara lotes de posts com validação e fila de agendamento. |
| [PostLab](plugins/postlab) | `criar-posts-criativos` | Criação de conteúdo | Cria peças, legendas e carrosséis para redes sociais. |
| [TokenMeter Universal](plugins/tokenmeter-universal) | `medir-tokens` | Produtividade | Registra e analisa consumo de tokens importado de metadados. |
| [Comparador de preços de carros](plugins/comparador-precos-carros) | `comparar-precos-carros` | Pesquisa | Compara preços de veículos no Brasil com critérios e fontes. |
| [Residência Radar Brasil](plugins/residencia-radar-brasil) | `residencia-radar` | Educação | Compara editais, vagas, notas e chamadas de residência médica. |
| [Edital Fácil](plugins/edital-facil) | `ler-editais` | Produtividade | Extrai requisitos, etapas e prazos de editais. |
| [ProvaLab](plugins/provalab) | `criar-avaliacoes` | Educação | Cria provas e estudos dirigidos com base em materiais enviados. |

| [InvestIA](plugins/investia) | `analisar-investimentos-ia` | Pesquisa financeira | Analisa fundamentos, notícias, cenários e riscos; simula posição à vista. |

## Os três novos plugins

### Residência Radar Brasil
Pesquisa programas por especialidade, estado e instituição. Organiza editais, vagas, concorrência, notas e convocações; compara ampla concorrência e PcD somente quando as fontes oficiais permitem comparação equivalente.

### Edital Fácil
Lê editais e retificações para destacar cargos, requisitos, remuneração, etapas, cotas, documentos e prazos, sempre apontando para o item ou página de origem.

### ProvaLab
Usa apostilas, slides e guias enviados para montar provas, simulados e estudos dirigidos. Mantém o gabarito separado conforme a solicitação e sinaliza qualquer conteúdo complementar.

## Instalação e uso

Cada diretório em `plugins/` é um pacote independente. Para usar uma skill em outro cliente compatível, copie `skills/<nome-da-skill>` para o local de skills indicado por esse cliente. Consulte o README de cada plugin para ver exemplos.

Os arquivos `plugin.json` descrevem o pacote. Os arquivos `.codex-plugin/plugin.json` mantêm metadados de compatibilidade do Codex. Skills que precisam consultar informações atuais orientam o assistente a pesquisar fontes vigentes e não contêm uma API própria.

## Segurança e qualidade

- Não coloque senhas, tokens ou chaves de API no repositório.
- Prefira fontes primárias e links verificáveis para informações públicas.
- Diferencie conteúdo do documento, cálculo e inferência.
- Não estime dados ausentes nem trate material educacional como aconselhamento profissional.

## Licença

Distribuído sob a licença [MIT](LICENSE).

<p align="center">Desenvolvido por <strong>Marlon Ferreira</strong></p>
