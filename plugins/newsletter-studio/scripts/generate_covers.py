import os
import glob
import urllib.request
import markdown

input_dir = r'C:\Users\marlo\asclepio-skills-and-plugins\scratch\viral'
output_dir = r'C:\Users\marlo\Downloads\Decifrando dados\Newsletter\BatchViral'

html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Preview da Newsletter</title>
<style>
  body { font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Fira Sans", Ubuntu, Oxygen, "Oxygen Sans", Cantarell, "Droid Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Lucida Grande", Helvetica, Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; color: #000; }
  .content-wrapper { border: 1px solid #ddd; padding: 40px; border-radius: 8px; background: #fff; margin-bottom: 20px; }
  .copy-button { display: block; width: 100%; padding: 15px; background: #0a66c2; color: white; border: none; border-radius: 24px; font-size: 16px; font-weight: bold; cursor: pointer; text-align: center; text-decoration: none; margin-bottom: 20px; }
  .copy-button:hover { background: #004182; }
  h1 { font-size: 24px; margin-bottom: 16px; }
  h2 { font-size: 20px; margin-top: 24px; margin-bottom: 16px; }
  p { margin-bottom: 16px; }
  ul { margin-bottom: 16px; }
  li { margin-bottom: 8px; }
  strong { font-weight: 600; }
  img { max-width: 100%; height: auto; border-radius: 8px; margin-bottom: 20px; display: block; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
</style>
</head>
<body>

<a href="https://www.linkedin.com/post/new" target="_blank" class="copy-button" onclick="copyRichText()">
  Copiar Texto Formatado e Abrir LinkedIn
</a>

<div class="content-wrapper" id="newsletter-content">
{content}
</div>

<script>
function copyRichText() {
    const content = document.getElementById('newsletter-content');
    const range = document.createRange();
    range.selectNodeContents(content);
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    
    document.execCommand('copy');
    
    selection.removeAllRanges();
    
    const btn = document.querySelector('.copy-button');
    const originalText = btn.innerText;
    btn.innerText = 'Copiado! 🎉';
    setTimeout(() => btn.innerText = originalText, 3000);
}
</script>
</body>
</html>"""

md_files = glob.glob(os.path.join(input_dir, '*.md'))

for i, md_file in enumerate(md_files):
    filename = os.path.basename(md_file)
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    img_filename = filename.replace('.md', '.jpg')
    img_path = os.path.join(output_dir, img_filename)
    
    # Force rewrite with picsum to avoid pollinations 402 error cache
    img_url = f"https://picsum.photos/seed/{i+42}/300/300"
    
    try:
        req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
            out_file.write(response.read())
        
        lines = text.split('\n')
        if lines[0].startswith('![Capa'):
            lines = lines[2:] # skip first two lines
        
        text = f"![Capa da Newsletter]({img_filename})\n\n" + '\n'.join(lines)
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(text)
            
    except Exception as e:
        print(f'Failed to download image for {filename}: {e}')
    
    html_content = markdown.markdown(text)
    final_html = html_template.replace('{content}', html_content)
    
    out_filename = filename.replace('.md', '.html')
    out_path = os.path.join(output_dir, out_filename)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f'[SUCESSO] Gerado com Capa Local: {out_filename}')
