import os
import click
import PyPDF2 as pdf

@click.command()
@click.argument('src')
@click.option('-s', '--suffix', type=str, default='notes')
def create_document(src, suffix):
    outfile_prefix = src.split('.pdf')[0]
    outfile_name = f'{outfile_prefix}_{suffix}.pdf'
    pdf_reader = pdf.PdfFileReader(src)
    pdf_writer = pdf.PdfFileWriter()

    for page_number in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page_number))
        pdf_writer.addBlankPage()

    with open(outfile_name, 'wb') as outfile:
        pdf_writer.write(outfile)

if __name__ == '__main__':
    create_document()

