import os
import markdown
from xhtml2pdf import pisa

def convert_md_to_pdf(md_path, pdf_path):
    print(f"[Gerador de PDF] Lendo o rascunho de: {md_path}")
    
    if not os.path.exists(md_path):
        print(f"[ERRO] Arquivo não encontrado: {md_path}")
        return False
        
    # Lê o conteúdo em Markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    # Converte Markdown para HTML
    # A extensão 'tables' ajuda caso tenha tabelas no markdown
    html_body = markdown.markdown(md_text, extensions=['tables'])
    
    # Monta a estrutura HTML básica com um CSS simples para o PDF ficar bonito
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            @page {{
                size: A4;
                margin: 2cm;
            }}
            body {{
                font-family: Helvetica, Arial, sans-serif;
                font-size: 14px;
                line-height: 1.6;
                color: #333333;
            }}
            h1, h2, h3 {{
                color: #1a1a1a;
                margin-top: 1.5em;
                margin-bottom: 0.5em;
            }}
            h1 {{ font-size: 24px; border-bottom: 1px solid #eeeeee; padding-bottom: 10px; }}
            h2 {{ font-size: 20px; }}
            h3 {{ font-size: 16px; }}
            p {{ margin-bottom: 1em; }}
            strong {{ color: #000000; }}
            hr {{ border: 0; border-top: 1px solid #eeeeee; margin: 2em 0; }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """
    
    # Cria e salva o arquivo PDF
    print(f"[Gerador de PDF] Gerando o arquivo {pdf_path}...")
    with open(pdf_path, "w+b") as result_file:
        # Converte HTML para PDF usando pisa (xhtml2pdf)
        pisa_status = pisa.CreatePDF(html_content, dest=result_file)
        
    if pisa_status.err:
        print("[ERRO] Falha ao gerar o PDF.")
        return False
        
    print(f"[SUCESSO] PDF gerado e salvo em: {os.path.abspath(pdf_path)}")
    return True

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    draft_md = os.path.join(base_dir, "scratch", "newsletter_draft.md")
    
    # Caminho onde o PDF será salvo
    output_dir = r"C:\Users\marlo\Downloads\Decifrando dados\Newsletter"
    os.makedirs(output_dir, exist_ok=True)
    output_pdf = os.path.join(output_dir, "newsletter_draft.pdf")
    
    sucesso = convert_md_to_pdf(draft_md, output_pdf)
    
    if sucesso:
        # Abre o PDF automaticamente no Windows
        try:
            os.startfile(output_pdf)
        except Exception as e:
            print(f"Não foi possível abrir o PDF automaticamente: {e}")
