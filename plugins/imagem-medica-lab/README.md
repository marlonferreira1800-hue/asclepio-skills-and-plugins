# Imagem Médica Lab

Inspecionar metadados DICOM, organizar séries, localizar bases públicas e avaliar qualidade técnica para pesquisa.

## Skills desta ampliação

| Skill | Função |
|---|---|
| [`inspecionar-dicom`](skills/inspecionar-dicom/SKILL.md) | Inspecionar metadados DICOM |
| [`organizar-series-dicom`](skills/organizar-series-dicom/SKILL.md) | Organizar séries DICOM |
| [`buscar-bases-imagens-medicas`](skills/buscar-bases-imagens-medicas/SKILL.md) | Buscar bases públicas de imagens |
| [`avaliar-qualidade-imagem-pesquisa`](skills/avaliar-qualidade-imagem-pesquisa/SKILL.md) | Avaliar qualidade técnica de imagens |

## Requisitos e execução

Arquivos autorizados e pydicom/visualizador quando necessários. Trabalhar localmente com dados sintéticos ou autorizados; não emite laudos.

Este pacote fornece instruções reutilizáveis. Não cria conexões, assinaturas, publicação ou execução automática. Os scripts incluídos estão documentados nas skills que os utilizam.

## Exemplos

- Inspecione tecnicamente estes DICOM sem mostrar dados de paciente.
- Agrupe estas imagens DICOM por série e verifique a ordem.
- Encontre bases públicas de imagens para estudar radiologia.
- Confira a qualidade técnica deste dataset de imagens.
