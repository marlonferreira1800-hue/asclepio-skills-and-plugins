# Verificação da ampliação — 2026-10-03

## Estrutura e utilitários

- 28 plugins e 94 skills encontrados no catálogo final.
- 79 novas skills passaram pelo `quick_validate.py` do Skill Creator.
- O validador local de catálogo encontrou zero erros e zero avisos.
- Sete testes automatizados passaram: exportação Unicode/HTML/TSV, cloze, rejeição de cartões inválidos, estrutura e exclusões do ZIP, recusa de sobrescrita/segredos/symlinks, referência ausente e divergência entre índice/overlay.
- Empacotamento do Anki Builder executado e integridade ZIP verificada.
- `git diff --check` passou.

O schema oficial Agent Plugins 1.0 foi consultado para o manifesto. A validação completa por JSON Schema não foi executada porque a biblioteca `jsonschema` não estava disponível. Os checks locais são um conjunto explícito de invariantes; não equivalem à validação integral do cliente.

## Exemplos de comportamento

Dois agentes independentes receberam as skills e tarefas concretas, sem resultados esperados:

1. **SQL Mentor — explicar-joins-sql:** executou consultas em SQLite com cliente sem pedido, cliente com dois pedidos, valores NULL e chaves sem correspondência. Explicou corretamente multiplicação de linhas, INNER versus LEFT JOIN e filtragem em ON versus WHERE. As consultas produziram respectivamente cinco, quatro e duas linhas nas condições testadas.
2. **Dados de Saúde Brasil — comparar-municipios-saude:** recebeu dados fictícios de notificações de um município e casos confirmados de outro. Calculou taxas de 400 por 100 mil para ambos, mas recusou atribuir maior incidência com definições diferentes. Explicou por que não somar internações SIH para contar pessoas únicas.

Esses casos avaliam dois fluxos específicos. Não foram executados todos os 79 workflows, consultas reais a APIs, sessões Power BI, importação Anki no aplicativo nem importação dos 28 pacotes em cada cliente. Instalações de conta não foram alteradas.
