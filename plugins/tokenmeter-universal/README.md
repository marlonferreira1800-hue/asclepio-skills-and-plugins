# TokenMeter Universal — skill + plugin portátil

Criado para Marlon Ferreira. Versão 1.0.0. Código aberto e execução local.

## O que funciona

- Registro persistente SQLite; relatórios por dia, semana, mês, ano e total acumulado.
- Entrada, saída, cache, raciocínio, total e categorias de qualidade, sem dupla contagem.
- Importação JSON/JSONL/CSV; adaptadores para respostas finais OpenAI/compatíveis, Claude, Gemini e Ollama.
- Filtros por provedor, aplicativo, conta/projeto e modelo; fuso padrão America/Sao_Paulo.
- Custos declarados ou tarifas configuradas por registro, moedas separadas e indicação de dados sem preço.
- Limite de tokens com aviso no relatório, backup JSON, exportação CSV e painel HTML estático.
- Skill em Markdown, plugin Agent Plugins 1.0 e servidor MCP local stdio com três ferramentas.

**Portabilidade não significa coleta automática em qualquer plataforma.** Clientes sem MCP precisam importar arquivos ou integrar o módulo ao aplicativo. O pacote não lê automaticamente seu perfil, histórico completo do ChatGPT, outras conversas nem consumo de outras contas. Valores informados por APIs são metadados da fonte, não auditoria de uma fatura. Estimativas nunca representam faturamento real.

## Executar no Windows, Linux ou macOS

1. Instalar Python 3.10 ou superior e extrair o pacote.
2. Abrir terminal na pasta tokenmeter-universal.
3. Executar `python -m pip install -r requirements.txt` (tzdata é necessário onde não há base de fusos do sistema).
4. Importar um arquivo real: `python skills/medir-tokens/scripts/tokenmeter.py import SEU_ARQUIVO.json`.
5. Abrir painel: `python skills/medir-tokens/scripts/tokenmeter.py dashboard --out painel.html` e abrir painel.html. No Windows, também há Abrir-TokenMeter.cmd.

Em sistemas que usam `python3`, substituir `python` por `python3`. O banco padrão é `~/.tokenmeter/usage.sqlite3`. Para mudar: definir TOKENMETER_DB ou passar `--db CAMINHO` antes do subcomando. Guardar o banco em lugar persistente, fora do repositório. Copiar o banco (com o processo fechado) ou exportar JSON para mudar de computador. Não publicar dados privados ou chaves no GitHub.

```sh
python skills/medir-tokens/scripts/tokenmeter.py report --period day
python skills/medir-tokens/scripts/tokenmeter.py report --period week
python skills/medir-tokens/scripts/tokenmeter.py report --period month
python skills/medir-tokens/scripts/tokenmeter.py report --period year
python skills/medir-tokens/scripts/tokenmeter.py report --period all
python skills/medir-tokens/scripts/tokenmeter.py report --period month --provider openai --budget-tokens 1000000
python skills/medir-tokens/scripts/tokenmeter.py export --format json --out backup.json
python skills/medir-tokens/scripts/tokenmeter.py export --format csv --out consumo.csv
python skills/medir-tokens/scripts/tokenmeter.py estimate --text "Texto para estimar"
```

Períodos seguem o calendário local; semanas começam segunda-feira. `--at 2026-09-30` escolhe data de referência; `--tz America/Porto_Velho` permite outro fuso. O painel é uma fotografia: gerar novamente para atualizar. O aviso de limite não bloqueia chamadas nem envia notificações.

## Testar com demonstração sem contaminar dados reais

```sh
python skills/medir-tokens/scripts/tokenmeter.py --db demo.sqlite3 import examples/usage-demo.json
python skills/medir-tokens/scripts/tokenmeter.py --db demo.sqlite3 report --period all
python skills/medir-tokens/scripts/tokenmeter.py --db demo.sqlite3 dashboard --at 2026-09-30 --out demo.html
python -m unittest discover -s tests -v
```

O arquivo demo contém dados fictícios explicitamente identificados, não o consumo do usuário. Não importar o exemplo no banco real.

## Coleta automática no seu próprio aplicativo

Inserir `examples/integracao_python.py` no aplicativo e chamar registrar_resposta após cada resposta final. Esse coletor não faz chamadas de IA, não exige chave e não monitora aplicativos terceiros. Usar ID estável por chamada e account/projeto para evitar duplicatas. Em streaming, registrar apenas metadados finais completos, sem somar snapshots cumulativos. Retentativas que tiveram consumo real são chamadas distintas. Não misturar exportações agregadas e eventos individuais do mesmo universo.

## Usar como plugin MCP

Clientes que aceitam Agent Plugins 1.0 descobrem plugin.json, skills/ e mcp.json. A expansão de ${PLUGIN_ROOT} depende do host. Em clientes que configuram MCP diretamente, adaptar examples/mcp-client.json com caminhos absolutos e o executável Python real. Ferramentas: record_usage, report_usage, estimate_text. O servidor usa JSON-RPC em linhas via stdin/stdout e não expõe porta de rede.

O ChatGPT web/mobile não executa um processo local apenas por importar este ZIP. Para integração hospedada, é necessário hospedar um adaptador MCP e configurar autenticação; essa hospedagem não faz parte deste pacote. Nem todas as plataformas aceitam o mesmo manifesto de plugin.

## Usar apenas a skill

Copiar skills/medir-tokens/ para o diretório de skills do cliente, quando houver suporte. Onde não houver suporte, usar SKILL.md como instruções e executar o medidor por terminal ou importar dados. A skill sozinha não habilita acesso a telemetria oculta.

## Custos e formato de dados

Ler skills/medir-tokens/references/contrato.md. Nenhum preço atual foi embutido. Usar cost_amount/currency informado ou rates com data e tarifas por milhão. Custos desconhecidos não são zero. Não misturar moedas, assinatura, preço por requisição e preço por token. CSV protege fórmulas e pode alterar strings perigosas; usar JSON para backup fiel.

A estimativa atual é caracteres/4, uma aproximação de texto. Não contabiliza multimodalidade, contexto oculto ou raciocínio e pode ter erro grande em idiomas/código. Contagem real exige metadados da fonte.

## Licença

MIT. Consulte LICENSE. A instalação em clientes terceiros e coleta real dependem da integração; testes automatizados verificam núcleo e protocolo local, sem chamadas reais pagas às APIs.
