---
name: medir-tokens
description: Medir e registrar tokens de IA por dia, semana, mês, ano e total acumulado. Usar para auditoria de consumo, importação CSV/JSON/JSONL, metadados OpenAI/compatíveis, Claude, Gemini e Ollama, custos configuráveis e estimativas de texto.
---

# TokenMeter Universal

Consultar [contrato e compatibilidade](references/contrato.md) antes de interpretar dados.

1. Identificar fonte, plataforma, conta/projeto, modelo, período e fuso. Usar America/Sao_Paulo por padrão; semanas começam segunda-feira.
2. Buscar metadados de consumo da fonte ou arquivos autorizados. Nunca alegar acesso a telemetria interna, perfil, outras conversas ou histórico completo sem ferramenta e dados que realmente os forneçam.
3. Usar ferramentas MCP TokenMeter quando disponíveis; com Python, executar `scripts/tokenmeter.py --help`. Definir TOKENMETER_DB para arquivo SQLite persistente autorizado, fora do código. Não publicar histórico privado no GitHub.
4. Registrar uma resposta final por chamada, com ID estável e account. Não somar snapshots cumulativos de streaming nem misturar relatórios agregados com chamadas do mesmo universo. Importar agregados em banco separado.
5. Separar reported (informado pela fonte), manual (digitado), estimated (heurística) e local_tokenizer (contagem do texto). Ausência de dados não comprova consumo zero.
6. Relatar entrada, saída, cache, raciocínio, total, quantidade de registros, origem e cobertura temporal. Cache é subconjunto da entrada; raciocínio é subconjunto da saída. Não somá-los novamente.
7. Calcular dinheiro apenas com custo declarado ou tarifas explícitas e datadas. Mostrar registros sem preço, separar moedas, não transformar assinatura em cobrança por token.
8. Estimar texto apenas como aproximação explicitamente identificada. Texto visível não representa necessariamente contexto, ferramentas, imagens, áudio ou raciocínio. Nunca chamar estimativa de faturamento real.
9. Exportar CSV/JSON ou painel HTML quando solicitado, no destino autorizado. Explicar adaptações necessárias se o cliente não suportar MCP ou execução de scripts. Instalação não ativa coleta automática.

## Operação

```sh
python scripts/tokenmeter.py import arquivo.json
python scripts/tokenmeter.py report --period day
python scripts/tokenmeter.py report --period week --at 2026-09-30
python scripts/tokenmeter.py report --period month
python scripts/tokenmeter.py report --period year
python scripts/tokenmeter.py report --period all
python scripts/tokenmeter.py export --format csv --out consumo.csv
python scripts/tokenmeter.py dashboard --out painel.html
python scripts/tokenmeter.py estimate --text 'Texto para estimar'
python scripts/tokenmeter.py mcp
```

Adaptar estas instruções para um prompt em clientes sem suporte a skills. O plugin local requer Python no computador do cliente; um upload de plugin não habilita execução local em navegador/mobile.
