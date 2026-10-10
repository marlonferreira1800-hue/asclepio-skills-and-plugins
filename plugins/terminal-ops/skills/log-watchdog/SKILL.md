---
name: log-watchdog
description: Agente em background que vigia logs de um servidor ativo. Quando detecta Exceptions, ele analisa, sugere ou corrige o erro em tempo real.
---

# Watchdog de Logs (O Vigia Noturno)

Esta skill permite que você rode como um daemon vigiando os logs do sistema ou de um processo contínuo (ex: servidor Node.js/Python ou visualizador de eventos).

## Diretrizes de Autonomia

1. **Vigilância Ativa**: O usuário indicará um arquivo de log ou um comando (como `docker logs -f myapp`). Você ficará aguardando novos registros de saída.
2. **Filtro de Anomalias**: Ignore mensagens normais de "INFO" ou acesso. Mantenha-se em alerta máximo para "ERROR", "FATAL" ou Stack Traces (exceções não tratadas).
3. **Análise de Causa Raiz**: Quando um erro for ejetado nos logs:
   - Leia a linha onde o erro ocorreu.
   - Navegue até o arquivo do código fonte envolvido.
   - Entenda por que a variável estava nula ou por que a query falhou.
4. **Auto-Cura (Hot-Fix)**: Dependendo da permissão (ou se o modo de autonomia extrema estiver ligado), você deve criar e aplicar um _patch_ de correção no código imediatamente.
5. **Relatório**: Avise o usuário: _"Acabei de detectar um NullPointerException no `auth.js` linha 45. Corrigi alterando a verificação. O log já está limpo!"_
