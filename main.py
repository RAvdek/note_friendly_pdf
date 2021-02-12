import click
import PyPDF2 as pdf

@click.command()
@click.argument('src')
def create_document(src):
    """Takes the `src` file, adds blanks every other page and creates a new file."""

    click.echo(f'Reading from file: {src}')
    outfile_prefix = src.split('.pdf')[0]
    outfile_name = f'{outfile_prefix}_notes.pdf'
    pdf_reader = pdf.PdfFileReader(src)
    pdf_writer = pdf.PdfFileWriter()

    for page_number in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page_number))
        pdf_writer.addBlankPage()

    click.echo(f'Writing to file: {outfile_name}')
    with open(outfile_name, 'wb') as outfile:
        pdf_writer.write(outfile)

if __name__ == '__main__':
    create_document()

