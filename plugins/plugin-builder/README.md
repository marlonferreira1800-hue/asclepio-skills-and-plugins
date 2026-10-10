# Plugin Builder

Estruturar plugins de skills, preparar manifestos, documentar requisitos e empacotar versões.

## Skills desta ampliação

| Skill                                                                    | Função                       |
| ------------------------------------------------------------------------ | ---------------------------- |
| [`estruturar-plugin`](skills/estruturar-plugin/SKILL.md)                 | Estruturar plugin            |
| [`preparar-manifesto-plugin`](skills/preparar-manifesto-plugin/SKILL.md) | Preparar manifesto de plugin |
| [`documentar-plugin`](skills/documentar-plugin/SKILL.md)                 | Documentar plugin            |
| [`empacotar-plugin`](skills/empacotar-plugin/SKILL.md)                   | Empacotar plugin             |

## Requisitos e execução

Sistema de arquivos e Python; validar com schema oficial ou validador do cliente quando disponível.

Este pacote fornece instruções reutilizáveis. Não cria conexões, assinaturas, publicação ou execução automática. Os scripts incluídos estão documentados nas skills que os utilizam.

## Exemplos

- Crie um plugin com três skills para análise de dados.
- Prepare o manifesto deste plugin para o formato Agent Plugins.
- Documente como instalar e usar este plugin de skills.
- Empacote este plugin em ZIP com os arquivos de compatibilidade.
