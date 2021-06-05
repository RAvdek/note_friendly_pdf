import click
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import PageObject


@click.command()
@click.argument('src')
@click.option('-s', '--selection', nargs=2, type=int, multiple=True, help='Page selection, start to end')
def create_document(src, selection):
    """Puts selected pages of a PDF in portrait mode with every other page blank"""

    click.echo(f'Reading from file: {src}')
    outfile_prefix = src.split('.pdf')[0]
    outfile_name = f'{outfile_prefix}_notes.pdf'

    pdf_reader = PdfFileReader(src)
    input_n_pages = pdf_reader.getNumPages()
    selected_page_numbers = list()
    if selection:
        for page_start_end in selection:
            page_start, page_end = page_start_end
            selected_page_numbers += range(page_start - 1, page_end)
        selected_page_numbers = list(set(selected_page_numbers))
        selected_page_numbers.sort()
    else:
        selected_page_numbers = [0, input_n_pages]
    click.echo(
        f'Preparing pages from source file between '
        f'p.{selected_page_numbers[0] + 1}-{selected_page_numbers[-1] + 1}'
    )

    pdf_writer = PdfFileWriter()

    for page_number in selected_page_numbers:
        page = pdf_reader.getPage(page_number)
        height = float(page.mediaBox.getHeight())
        width = float(page.mediaBox.getWidth())
        hw_scale = height / width
        new_page = PageObject.createBlankPage(height=height, width=width)
        new_page.mergeRotatedScaledTranslatedPage(page, 90, 1.0 / hw_scale, width, 0, expand=False)
        new_page.rotateClockwise(90)
        pdf_writer.addPage(new_page)

    click.echo(f'Writing to file: {outfile_name}')
    with open(outfile_name, 'wb') as outfile:
        pdf_writer.write(outfile)


if __name__ == '__main__':
    create_document()

