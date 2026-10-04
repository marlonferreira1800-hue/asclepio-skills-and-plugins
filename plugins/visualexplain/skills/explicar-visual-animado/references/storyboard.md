# Contrato do roteiro v1

JSON UTF-8 com `title` (string) e `scenes` (lista não vazia).
Cada cena: `title`, `explanation`, `steps` (lista de 1–6 strings curtas), `source` (localizador legível).
Cada passo representa uma etapa de um processo ou raciocínio, exibida em ordem.
O modelo renderiza um fluxo progressivo; pode ser ampliado para diagramas SVG específicos.
Não inserir HTML em campos; o renderizador trata conteúdo como texto.

Exemplo de uso: ler um capítulo → selecionar mecanismo → criar 6 cenas → citar página de cada cena → gerar HTML → conferir com o documento.

Extensões planejadas, ainda não implementadas: extratores automáticos por formato, OCR integrado, narração, vídeo MP4, gráficos dinâmicos e painel de upload. A skill delega leitura e raciocínio ao agente e às ferramentas disponíveis.
