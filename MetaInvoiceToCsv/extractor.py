import PyPDF2 

def getText(pdf_file):
    texto = ''
    with open(pdf_file, 'rb') as input_pdf:
        arq = PyPDF2.PdfReader(input_pdf)

        for pagina in arq.pages:
            texto += pagina.extract_text()
    return texto