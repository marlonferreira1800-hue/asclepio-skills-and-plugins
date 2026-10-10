# LinkedIn Post Design Kit

Scaffold de um plugin de instruções e uma skill para planejar conteúdo e criar peças visuais para LinkedIn, usando dez repositórios de design como referências.

## Estrutura

```text
linkedin-post-design-kit/
├── plugin.json
├── README.md
└── skills/
    └── linkedin-post-designer/
        ├── SKILL.md
        ├── references/
        │   └── repositories.md
        └── templates/
            └── post-brief.md
```

## Componentes

- `plugin.json`: nome, descrição e prompt curto do plugin.
- `SKILL.md`: fluxo para entender o pedido, escolher formato, criar conteúdo, orientar o design e revisar a peça.
- `references/repositories.md`: dez fontes organizadas por função, com critérios para conferir atividade e licenças.
- `templates/post-brief.md`: campos opcionais para orientar a criação.

## O que ele faz e o que precisa de integração

O pacote contém uma skill de instruções. Por si só, não abre o Penpot, não busca automaticamente os repositórios e não publica no LinkedIn. Quando ferramentas de navegação ou geração visual estiverem disponíveis, a skill pode usá-las; caso contrário, deve indicar com clareza o que não conseguiu consultar ou gerar. Não invente que verificou uma fonte.
