#!/usr/bin/env python3
"""Compilador oficial de edições da newsletter 'Decifrando Dados'.

Gera:
1. Arquivo HTML estilizado e responsivo.
2. Arquivo PDF profissional de alta resolução (via Edge Headless).
3. Arquivo formatado para cópia direta no editor de Artigos do LinkedIn.
4. Opcionalmente envia o Artigo do LinkedIn para a Área de Transferência (Clipboard).
"""

import argparse
import html
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def parse_markdown_to_html(md_text: str) -> tuple[dict, str, str]:
    """Extrai metadados, corpo HTML para o PDF e texto limpo para o LinkedIn."""
    metadata = {
        "titulo": "Edição da Semana",
        "subtitulo": "Ciência de Dados, Machine Learning e IA na Prática",
        "edicao": "01",
        "data": datetime.now().strftime("%d/%m/%Y"),
        "tempo_leitura": "3",
    }

    lines = md_text.splitlines()
    body_lines = []
    in_frontmatter = False
    frontmatter_read = False

    # Checar frontmatter YAML com suporte a multilinha
    current_key = None
    multiline_buf = []

    for i, line in enumerate(lines):
        striped = line.strip()
        if i == 0 and striped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if striped == "---":
                if current_key and multiline_buf:
                    metadata[current_key] = "\n".join(multiline_buf).strip()
                in_frontmatter = False
                frontmatter_read = True
                continue
            if re.match(r"^[a-zA-Z0-9_\-]+:", line):
                if current_key and multiline_buf:
                    metadata[current_key] = "\n".join(multiline_buf).strip()
                    multiline_buf = []
                k, v = line.split(":", 1)
                current_key = k.strip().lower()
                val = v.strip().strip('"').strip("'")
                if val in ("|", ">", ""):
                    multiline_buf = []
                else:
                    metadata[current_key] = val
                    current_key = None
            elif current_key is not None:
                # Manter linhas vazias para parágrafos no post
                multiline_buf.append(line.strip())
            continue
        body_lines.append(line)

    body_md = "\n".join(body_lines).strip()

    # Se metadados não vieram no frontmatter, tentar inferir do Markdown
    m_h1 = re.search(r"^#\s+(.+)$", body_md, re.MULTILINE)
    if m_h1 and metadata.get("titulo") == "Edição da Semana":
        metadata["titulo"] = m_h1.group(1).strip()

    m_h2 = re.search(r"^##\s+(.+)$", body_md, re.MULTILINE)
    if m_h2 and metadata.get("subtitulo") == "Ciência de Dados, Machine Learning e IA na Prática":
        metadata["subtitulo"] = m_h2.group(1).strip()

    # Processar HTML do corpo
    html_out = []
    in_list = False
    in_code = False
    code_block = []

    for line in body_lines:
        # Se for título H1 ou H2 inicial, não duplicar se já foi para o cabeçalho
        if line.startswith("# ") and metadata["titulo"] in line:
            continue
        if line.startswith("## ") and metadata["subtitulo"] in line:
            continue

        # Blocos de código
        if line.startswith("```"):
            if in_code:
                in_code = False
                html_out.append(f"<pre><code>{html.escape(chr(10).join(code_block))}</code></pre>")
                code_block = []
            else:
                if in_list:
                    html_out.append("</ul>")
                    in_list = False
                in_code = True
            continue

        if in_code:
            code_block.append(line)
            continue

        # Linhas horizontais
        if re.match(r"^---+$", line.strip()):
            if in_list:
                html_out.append("</ul>")
                in_list = False
            html_out.append("<hr style='border:none;border-top:1px solid #E2E8F0;margin:24px 0;'>")
            continue

        # Headings
        if line.startswith("### "):
            if in_list:
                html_out.append("</ul>")
                in_list = False
            title = line[4:].strip()
            html_out.append(f"<h2>{format_inline(title)}</h2>")
            continue
        elif line.startswith("#### "):
            if in_list:
                html_out.append("</ul>")
                in_list = False
            title = line[5:].strip()
            html_out.append(f"<h3>{format_inline(title)}</h3>")
            continue

        # Listas
        if re.match(r"^\s*[\*\-]\s+(.+)$", line):
            m = re.match(r"^\s*[\*\-]\s+(.+)$", line)
            if not in_list:
                html_out.append("<ul>")
                in_list = True
            html_out.append(f"<li>{format_inline(m.group(1))}</li>")
            continue
        else:
            if in_list:
                html_out.append("</ul>")
                in_list = False

        # Blockquote / Callout
        if line.startswith("> "):
            content = line[2:].strip()
            if "🎯" in content or "Na prática" in content.lower():
                html_out.append(f"<div class='callout callout-pratica'>{format_inline(content)}</div>")
            elif "💡" in content or "destaque" in content.lower():
                html_out.append(f"<div class='callout callout-destaque'>{format_inline(content)}</div>")
            else:
                html_out.append(f"<blockquote>{format_inline(content)}</blockquote>")
            continue

        # Parágrafos
        if line.strip():
            html_out.append(f"<p>{format_inline(line.strip())}</p>")

    if in_list:
        html_out.append("</ul>")

    # Gerar versão para Artigo do LinkedIn
    article_text = generate_linkedin_article(metadata, body_md)

    return metadata, "\n".join(html_out), article_text


def format_inline(text: str) -> str:
    """Formata negrito, itálico e links inline para HTML."""
    text = html.escape(text)
    # Reverter escape de tags intencionais
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def generate_linkedin_article(metadata: dict, body_md: str) -> str:
    """Gera pacote completo para publicação no LinkedIn: SEO, Post de Divulgação e Artigo."""
    titulo = metadata.get("titulo", "Edição da Semana")
    subtitulo = metadata.get("subtitulo", "Ciência de Dados, Machine Learning e IA na Prática")
    edicao = metadata.get("edicao", "01")
    
    # Metadados de SEO
    seo_titulo = metadata.get("seo_titulo") or metadata.get("titulo_seo") or titulo
    seo_descricao = metadata.get("seo_descricao") or metadata.get("descricao_seo") or (
        f"{subtitulo} Entenda os impactos práticos e tendências de Dados e IA na sua carreira."
    )
    
    # Post de divulgação
    post_divulgacao = metadata.get("post_divulgacao") or (
        f"O mercado de tecnologia e dados mudou de patamar. Quem opera apenas no modo automático está perdendo relevância.\n\n"
        f"Nesta edição da Decifrando Dados, analiso na prática: {titulo}.\n\n"
        f"Leia a edição completa abaixo e me conte nos comentários: como você vê essa transformação no seu dia a dia?\n\n"
        f"#dados #analytics #carreira #ia #sql #DecifrandoDados"
    )

    clean_body = []
    for line in body_md.splitlines():
        if line.startswith("---") or line.startswith("title:") or line.startswith("edition:") or line.startswith("seo_"):
            continue
        clean_body.append(line)

    package = [
        "=" * 70,
        f"DECIFRANDO DADOS - EDIÇÃO {edicao}",
        "=" * 70,
        "",
        "⚙️ Metadados de SEO para o LinkedIn",
        f"Título SEO: {seo_titulo}",
        "",
        f"Descrição SEO: {seo_descricao}",
        "",
        "* Copie estes dados manualmente para a área de SEO do LinkedIn. O texto do artigo está logo abaixo.",
        "",
        "-" * 70,
        '📢 Post de Divulgação ("Conte para sua rede..."):',
        "-" * 70,
        post_divulgacao.strip(),
        "",
        "=" * 70,
        "[CONTEÚDO DO ARTIGO PARA COPIAR E COLAR]:",
        "=" * 70,
        "",
        f"[TÍTULO DO ARTIGO NO LINKEDIN]:",
        titulo,
        "",
        f"[SUBTÍTULO / SLOGAN]:",
        subtitulo,
        "",
        "-" * 70,
        "",
        "\n".join(clean_body).strip(),
        "",
        "=" * 70,
    ]

    return "\n".join(package)


def compile_pdf(html_path: Path, pdf_path: Path) -> bool:
    """Compila o arquivo HTML para PDF usando o Microsoft Edge headless nativo."""
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]

    edge_exe = None
    for p in edge_paths:
        if os.path.exists(p):
            edge_exe = p
            break

    if not edge_exe:
        print("Aviso: Microsoft Edge não encontrado nos caminhos padrão.", file=sys.stderr)
        return False

    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path.resolve()}",
        f"file:///{html_path.resolve()}",
    ]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return pdf_path.exists()
    except Exception as e:
        print(f"Erro ao compilar PDF: {e}", file=sys.stderr)
        return False


def copy_to_clipboard(text: str) -> bool:
    """Copia o conteúdo para a área de transferência do Windows."""
    try:
        process = subprocess.Popen(
            ["powershell", "-NoProfile", "-Command", "$input | Set-Clipboard"],
            stdin=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )
        process.communicate(input=text)
        return process.returncode == 0
    except Exception as e:
        print(f"Erro ao copiar para clipboard: {e}", file=sys.stderr)
        return False


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Compilador da Newsletter Decifrando Dados")
    parser.add_argument("--input", "-i", required=True, help="Arquivo Markdown da edição")
    parser.add_argument("--output-dir", "-o", default=r"C:\Users\marlo\Downloads\dados25", help="Diretório de saída")
    parser.add_argument("--template", "-t", default=None, help="Caminho do template HTML")
    parser.add_argument("--pdf", action="store_true", help="Gerar arquivo PDF")
    parser.add_argument("--copy", action="store_true", help="Copiar artigo do LinkedIn para a Área de Transferência")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"Erro: Arquivo não encontrado: {input_path}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Localizar template HTML
    template_path = Path(args.template) if args.template else Path(__file__).parent / "template.html"
    if not template_path.exists():
        print(f"Erro: Template HTML não encontrado em {template_path}", file=sys.stderr)
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_html = f.read()

    metadata, body_html, article_linkedin = parse_markdown_to_html(md_content)

    # Preencher template
    titulo = metadata.get("titulo", "Edição")
    subtitulo = metadata.get("subtitulo", "")
    seo_titulo = metadata.get("seo_titulo") or metadata.get("titulo_seo") or titulo
    seo_descricao = metadata.get("seo_descricao") or metadata.get("descricao_seo") or (
        f"{subtitulo} Entenda os impactos práticos e tendências de Dados e IA na sua carreira."
    )
    post_divulgacao = metadata.get("post_divulgacao") or ""

    filled_html = template_html
    filled_html = filled_html.replace("{{TITULO}}", titulo)
    filled_html = filled_html.replace("{{SUBTITULO}}", subtitulo)
    filled_html = filled_html.replace("{{EDICAO}}", str(metadata.get("edicao", "01")))
    filled_html = filled_html.replace("{{DATA}}", metadata.get("data", datetime.now().strftime("%d/%m/%Y")))
    filled_html = filled_html.replace("{{TEMPO_LEITURA}}", str(metadata.get("tempo_leitura", "3")))
    filled_html = filled_html.replace("{{SEO_TITULO}}", html.escape(seo_titulo))
    filled_html = filled_html.replace("{{SEO_DESCRICAO}}", html.escape(seo_descricao))
    filled_html = filled_html.replace("{{POST_DIVULGACAO}}", html.escape(post_divulgacao).replace("\n", "<br>"))
    filled_html = filled_html.replace("{{CONTEUDO_HTML}}", body_html)

    base_name = input_path.stem
    html_output = output_dir / f"{base_name}.html"
    pdf_output = output_dir / f"{base_name}.pdf"
    article_output = output_dir / f"{base_name}_artigo_linkedin.txt"

    # Salvar HTML
    with open(html_output, "w", encoding="utf-8") as f:
        f.write(filled_html)
    print(f"[OK] HTML gerado com sucesso: {html_output}")

    # Salvar Artigo LinkedIn
    with open(article_output, "w", encoding="utf-8") as f:
        f.write(article_linkedin)
    print(f"[OK] Artigo LinkedIn pronto para cópia: {article_output}")

    # Compilar PDF
    if args.pdf:
        success = compile_pdf(html_output, pdf_output)
        if success:
            print(f"[OK] PDF compilado com sucesso: {pdf_output}")
        else:
            print("! Falha ao compilar PDF.", file=sys.stderr)

    # Copiar para Clipboard
    if args.copy:
        if copy_to_clipboard(article_linkedin):
            print("[OK] Artigo do LinkedIn copiado para a Área de Transferência (Ctrl+V pronto para uso)!")


if __name__ == "__main__":
    main()
