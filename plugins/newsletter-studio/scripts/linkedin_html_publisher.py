import os
import markdown
import webbrowser
from datetime import datetime

def generate_interactive_html(md_path, output_html):
    if not os.path.exists(md_path):
        print(f"[ERRO] Rascunho não encontrado: {md_path}")
        return False
        
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    html_body = markdown.markdown(md_text, extensions=['tables'])
    
    html_page = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Preview da Newsletter</title>
    <style>
        body {{
            font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Fira Sans", Ubuntu, Oxygen, "Oxygen Sans", Cantarell, sans-serif;
            line-height: 1.5;
            color: rgba(0,0,0,0.9);
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background: #f3f2ef;
        }}
        .container {{
            background: #ffffff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 0 1px rgba(0,0,0,0.08);
        }}
        .toolbar {{
            position: sticky;
            top: 20px;
            margin-bottom: 20px;
            text-align: right;
            z-index: 100;
        }}
        .btn {{
            background: #0a66c2;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 24px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: background 0.2s;
            text-decoration: none;
            display: inline-block;
        }}
        .btn:hover {{
            background: #004182;
        }}
        
        #content h1 {{ font-size: 24px; font-weight: 600; margin: 24px 0 16px; }}
        #content h2 {{ font-size: 20px; font-weight: 600; margin: 24px 0 16px; }}
        #content h3 {{ font-size: 18px; font-weight: 600; margin: 24px 0 16px; }}
        #content p {{ margin-bottom: 16px; font-size: 16px; }}
        #content ul {{ margin-bottom: 16px; padding-left: 24px; }}
        #content li {{ margin-bottom: 8px; font-size: 16px; }}
        #content img {{ max-width: 100%; height: auto; border-radius: 8px; margin: 16px 0; display: block; }}
    </style>
</head>
<body>
    <div class="toolbar">
        <a href="https://www.linkedin.com/article/new/" target="_blank" class="btn" id="copyBtn" onclick="copyContent(this)">1. Copiar Formatação e 2. Abrir LinkedIn</a>
    </div>
    <div class="container" id="content">
        {html_body}
    </div>

    <script>
        function copyContent(linkElement) {{
            const contentDiv = document.getElementById('content');
            
            const range = document.createRange();
            range.selectNodeContents(contentDiv);
            
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
            
            try {{
                document.execCommand('copy');
                linkElement.innerHTML = '✔ Copiado! Agora cole (Ctrl+V) na nova aba do LinkedIn';
                linkElement.style.background = '#057642'; // Verde
                setTimeout(function() {{
                    selection.removeAllRanges();
                }}, 100);
            }} catch (err) {{
                alert('Erro ao copiar: ' + err);
            }}
        }}
    </script>
</body>
</html>
"""
    
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_page)
        
    print(f"[SUCESSO] Preview interativo gerado: {output_html}")
    return True

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    draft_md = os.path.join(base_dir, "scratch", "newsletter_draft.md")
    
    output_dir = r"C:\Users\marlo\Downloads\Decifrando dados\Newsletter"
    os.makedirs(output_dir, exist_ok=True)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_html = os.path.join(output_dir, f"Newsletter_Preview_{date_str}.html")
    
    sucesso = generate_interactive_html(draft_md, output_html)
    
    if sucesso:
        webbrowser.open('file://' + os.path.realpath(output_html))
