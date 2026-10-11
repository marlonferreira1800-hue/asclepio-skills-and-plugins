import os
import glob

output_dir = r'C:\Users\marlo\Downloads\Decifrando dados\Newsletter\BatchViral'

seo_data = {
    'newsletter_01_junior.html': ('O Fim do Analista de Dados Júnior e o Impacto da IA', 'Com o avanço de IAs como o Copilot, o mercado para analistas de dados juniores mudou. Entenda como adaptar sua carreira e evitar ser substituído por robôs.'),
    'newsletter_02_excel.html': ('IA Corporativa vs Excel: A Realidade da Área de Dados', 'Sua empresa exige inteligência artificial, mas ainda opera em planilhas Excel quebradas? Descubra a importância de uma governança sólida na engenharia de dados.'),
    'newsletter_03_datadriven.html': ('O Mito da Cultura Data-Driven nas Empresas Modernas', 'Sua empresa é realmente data-driven ou usa análise de dados apenas para justificar decisões por feeling? Descubra como quebrar o teatro e focar na engenharia.'),
    'newsletter_04_dashboards.html': ('A Morte dos Dashboards Complexos em Análise de Dados', 'Profissionais de BI gastam meses criando dashboards complexos que ninguém acessa. Descubra por que a engenharia de dados moderna exige soluções mais diretas.'),
    'newsletter_05_certs.html': ('Certificações Cloud (AWS, GCP) vs Experiência em Dados', 'Ter dezenas de certificações em nuvem não garante emprego na área de engenharia de dados. Entenda por que a experiência prática e arquitetura cloud importam.'),
    'newsletter_06_titles.html': ('A Inflação de Cargos e o Falso Cientista de Dados', 'Descubra como a inflação de títulos prejudica o mercado de tecnologia. Ser cientista de dados exige muito mais do que rodar um modelo simples no scikit-learn.'),
    'newsletter_07_pythonsql.html': ('Python vs SQL: O Erro Comum na Engenharia de Dados', 'Por que engenheiros de dados complicam pipelines com código Python quando um SQL nativo seria mais rápido e barato? Aprenda como evitar excesso de engenharia.'),
    'newsletter_08_salaries.html': ('O Fim da Bolha Salarial em Dados e Tecnologia', 'Os salários absurdos da área de dados na pandemia acabaram. Entenda a correção do mercado tech e como engenheiros e cientistas podem garantir sua relevância.'),
    'newsletter_09_gov.html': ('Governança de Dados: A Base Lucrativa da Inteligência', 'Todo mundo foca em IA, mas o verdadeiro lucro na área tech está na governança e qualidade de dados. Descubra como essa área não-sexy sustenta grandes empresas.'),
    'newsletter_10_bootcamps.html': ('A Ilusão dos Bootcamps na Carreira de Dados e Tech', 'Fuja de falsas promessas de salários astronômicos em seis meses. Entenda a realidade do mercado tech e o que realmente constrói uma carreira sólida em dados.')
}

html_files = glob.glob(os.path.join(output_dir, '*.html'))

for html_file in html_files:
    filename = os.path.basename(html_file)
    if filename in seo_data:
        title, desc = seo_data[filename]
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'class="seo-box"' in content:
            continue
            
        seo_html = f'''
<div class="seo-box" style="background: #f8f9fa; border-left: 4px solid #0a66c2; padding: 20px; margin-bottom: 20px; border-radius: 4px; font-family: sans-serif;">
    <h3 style="margin-top: 0; color: #0a66c2;">⚙️ Metadados de SEO para o LinkedIn</h3>
    <p><strong>Título SEO:</strong> {title}</p>
    <p><strong>Descrição SEO:</strong> {desc}</p>
    <p style="font-size: 12px; color: #666;">* Copie estes dados manualmente para a área de SEO do LinkedIn. O botão azul copiará apenas o texto do artigo.</p>
</div>
'''
        
        split_marker = '<div class="content-wrapper"'
        if split_marker in content:
            parts = content.split(split_marker)
            new_content = parts[0] + seo_html + split_marker + parts[1]
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'SEO Injetado: {filename}')
