import os
import subprocess
import tempfile

def hybrid_drafter():
    print("[Iniciando a Rota Hibrida Inteligente - RPA Nativo]")
    
    draft_path = os.path.join("scratch", "newsletter_draft.md")
    if not os.path.exists(draft_path):
        print("[Erro] Arquivo de rascunho nao encontrado.")
        return

    print("[Copiando] Jogando a newsletter pronta para a sua area de transferencia...")
    
    # Criamos um script PowerShell rápido para interagir nativamente com o Windows
    ps_script = f"""
    # Lê o rascunho e joga no clipboard preservando quebras de linha
    Get-Content -Path "{draft_path}" -Encoding UTF8 -Raw | Set-Clipboard
    
    # Abre o navegador padrão (seu Chrome/Edge onde já está logado) direto na página de edição
    Start-Process "https://www.linkedin.com/article/new/"
    """
    
    # Salva e executa o script PowerShell
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ps1", mode='w', encoding='utf-8') as f:
        f.write(ps_script)
        temp_path = f.name
        
    try:
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", temp_path], check=True)
        print("[Sucesso]")
        print("O seu navegador abriu na tela de edicao do LinkedIn.")
        print("Basta clicar na caixa de texto e apertar 'Ctrl + V'.")
    finally:
        os.remove(temp_path)

if __name__ == "__main__":
    hybrid_drafter()
