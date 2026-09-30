# Contrato, compatibilidade e fontes

Python 3.10+, SQLite padrão, zoneinfo. No Windows, instalar tzdata se necessário. Não são necessárias chaves para importar dados. Não há acesso automático a perfis, conversas ou outras contas.

Formato canônico: id, timestamp ISO 8601 com fuso, provider, platform, account, model, input_tokens, output_tokens, cached_input_tokens, cache_write_tokens, reasoning_tokens, other_tokens, total_tokens, quality, source. Total = entrada + saída + outros; cache e raciocínio já são subconjuntos. Identidade = provider + platform + account + id. Reimportação idêntica é ignorada; conflito é erro. Sem ID, hash do registro normalizado completo. Fornecer ID estável na integração para deduplicar.

quality: reported = metadados informados pela fonte, sem auditoria contra fatura; manual = digitado; estimated = caracteres/4; local_tokenizer = contagem do texto por tokenizer específico, não consumo faturado.

Importar JSON de um registro, lista JSON, JSONL ou CSV canônico. Envelope de resposta API: {"provider":"openai","platform":"meu-app","account":"projeto-1","timestamp":"2026-09-30T16:00:00-03:00","response":{...resposta final...}}. Para Claude/Gemini usar provider anthropic/gemini. Sem data, usar hora da importação com aviso; dados históricos precisam de timestamp. Importação transacional: um erro reverte todo o lote.

OpenAI Responses: usage.input_tokens/output_tokens. cached_tokens/cache_write_tokens são subconjuntos da entrada; reasoning_tokens da saída. Chat Completions/compatíveis: prompt_tokens/completion_tokens. Claude: entrada = input_tokens + cache_read_input_tokens + cache_creation_input_tokens. Gemini: entrada promptTokenCount; saída candidatesTokenCount + thoughtsTokenCount; respeitar totalTokenCount informado e guardar diferença não atribuída como other_tokens. Ollama: prompt_eval_count/eval_count. Outros provedores: canônico ou compatível OpenAI. Recusar contagens negativas, fracionárias e parciais; não aceitar snapshots de streaming como chamadas adicionais.

UTC no armazenamento; calendário local nos relatórios, intervalo [início, fim). Semana segunda a segunda; mês e ano calendários. Total acumulado cobre apenas registros importados. Não consolidar universos sobrepostos sem reconciliação.

Custos opcionais: cost_amount/currency ou rates com currency, as_of (data ISO), input_per_million, cached_per_million, cache_write_per_million e output_per_million. Categoria usada sem tarifa torna custo desconhecido. Tarifas guardadas por evento; não incluir automaticamente impostos, ferramentas, descontos ou câmbio. Budget tokens é aviso no relatório, não bloqueio nem notificação em segundo plano.

MCP stdio: record_usage, report_usage, estimate_text. Clientes precisam suportar servidor local e configurar Python/caminho. ChatGPT web/mobile não executa servidor local apenas por importar plugin. SKILL.md pode ser usado como instruções em outras plataformas; nenhum manifesto é universalmente aceito.

CSV exportado protege strings de fórmulas em planilhas; JSON preserva o registro para backup/reimportação fiel.

Fontes oficiais consultadas em 2026-09-30:
- https://developers.openai.com/api/docs/guides/token-counting
- https://developers.openai.com/api/docs/guides/prompt-caching
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- https://ai.google.dev/api/generate-content#UsageMetadata
- https://modelcontextprotocol.io/specification/2025-03-26/basic/transports
