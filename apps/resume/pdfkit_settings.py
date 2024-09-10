import pdfkit
from django.conf import settings
from django.templatetags.static import static


wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

PDFKIT_OPTIONS = {
    'page-size': 'A4',
    'encoding': 'UTF-8',
    'no-outline': None,
    'quiet': '',
    'enable-local-file-access': '',
    'zoom': '1.0',
    '--enable-local-file-access': '', 
}

pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

def generate_pdf_from_html(html_content, output_path=None):
    pdf = pdfkit.from_string(html_content, output_path, configuration=pdfkit_config, options=PDFKIT_OPTIONS)
    return pdf


