"""
Iniciador Autonomo de Newsletter 'Decifrando Dados' via AGY
Desenvolvido para Marlon Ferreira.
Pede apenas o link, arquivo ou tema e dispara o AGY com permissao total e receita de bolo.
"""

import sys
import os
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

AGY_PATH = r"C:\Users\marlo\AppData\Local\agy\bin\agy.exe"

BANNER = r"""
==============================================================================
  📰 DECIFRANDO DADOS  •  GERADOR 100% AUTÔNOMO DE NEWSLETTER (AGY)
==============================================================================
  Curadoria: Marlon Ferreira  •  Formato: The BRIEF  •  Pipeline Oficial
==============================================================================
"""

def main():
    print(BANNER)
    print(" Insira a pauta da sua nova edição.")
    print(" Pode ser um LINK de notícia, caminho de ARQUIVO ou apenas o TEMA:\n")
    
    try:
        entrada = input(" 🎯 Cole aqui o Link / Arquivo / Tema: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nOperação cancelada.")
        return

    if not entrada:
        print("\n❌ Nenhuma entrada informada. Encerrando.")
        return

    print("\n" + "─" * 78)
    print(f" 🚀 Iniciando o AGY em Modo Autônomo com a sua pauta...")
    print("─" * 78 + "\n")

    # Prompt rigoroso com a receita de bolo oficial
    super_prompt = (
        f'Crie a nova edição completa da newsletter oficial Decifrando Dados seguindo estritamente '
        f'a RECEITA_DE_BOLO_NEWSLETTER.md e o formato The BRIEF com base neste link/arquivo/tema: "{entrada}".\n\n'
        f'DIRETRIZES OBRIGATÓRIAS:\n'
        f'1. Formato The BRIEF ("Smart people are cooler" - ágil, sarcástico, dados reais mastigados e zero corporatiquês).\n'
        f'2. Estrutura milimétrica: Frontmatter YAML, Efeméride histórica conectada à pauta, Índice Âncora (⚡ O que você vai ver hoje), '
        f'Matéria de Capa em caixa alta com destaque (💡 O número do jogo) e provocação (🎯 Recado para a diretoria), '
        f'Don\'t Leave Just Read (giro de 3 a 4 notícias curtas com emojis), Decifrando na Prática (3 passos técnicos acionáveis), '
        f'A Redação Recomenda e Frase do Dia.\n'
        f'3. Bloco de Topo Obrigatório: Metadados de SEO para o LinkedIn (Título e Descrição de 140-160 caracteres com aviso do botão azul) '
        f'e Post de Divulgação ("Conte para sua rede...") com gancho forte e hashtags #dados #analytics #carreira #ia #sql.\n'
        f'4. Filtro Anticlichê: Proibido termos vazios (mergulhar, revolucionário, crucial, panorama, testamento, no fim das contas).\n'
        f'5. Forno / Compilação: Compile imediatamente o markdown gerado com o build_newsletter.py gerando o PDF diagramado em '
        f'C:\\Users\\marlo\\Downloads\\dados25, o HTML com toolbar e copiando o texto para a Área de Transferência.\n'
        f'6. Execute tudo de forma 100% autônoma até a entrega final completa.'
    )

    # Executa o AGY com auto-aprovação de ferramentas
    cmd = [
        AGY_PATH,
        "--dangerously-skip-permissions",
        "-i",
        super_prompt
    ]

    try:
        subprocess.run(cmd)
    except Exception as e:
        print(f"\n❌ Erro ao disparar o AGY: {e}")

if __name__ == "__main__":
    main()
