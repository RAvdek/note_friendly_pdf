import sys
import click
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject

@click.command()
@click.argument('src')
@click.option('-s', '--start_page', type=int, help='Start reading at this page number')
@click.option('-e', '--end_page', type=int, help='Stop reading after this page number')
def create_document(src, start_page, end_page):
    """Takes the `src` file, adds blanks every other page and creates a new file."""

    click.echo(f'Reading from file: {src}')
    outfile_prefix = src.split('.pdf')[0]
    outfile_name = f'{outfile_prefix}_notes.pdf'

    pdf_reader = PdfFileReader(src)
    input_n_pages = pdf_reader.getNumPages()
    page_range = [
        start_page - 1 if start_page else 0,
        end_page if end_page else input_n_pages]
    click.echo(f'Preparing pages from source file: p.{page_range[0]}-{page_range[1]}')

    pdf_writer = PdfFileWriter()

    for page_number in range(*page_range):
        page = pdf_reader.getPage(page_number)
        height = page.mediaBox.getHeight()
        width = page.mediaBox.getWidth()
        hw_scale = 1.0*height / width
        new_page = PageObject.createBlankPage(height=height, width=width)
        new_page.mergeRotatedScaledTranslatedPage(page, 90, 1.0 / hw_scale, width, 0, expand=False)
        new_page.rotateClockwise(90)
        pdf_writer.addPage(new_page)

    click.echo(f'Writing to file: {outfile_name}')
    with open(outfile_name, 'wb') as outfile:
        pdf_writer.write(outfile)

if __name__ == '__main__':
    create_document()

