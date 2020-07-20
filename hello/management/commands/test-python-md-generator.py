from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from markdowngenerator import MarkdownGenerator


class Command(BaseCommand):
    help = 'Merge airport name and code'

    def handle(self, *args, **options):
        with MarkdownGenerator(
                # By setting enable_write as False, content of the file is written
                # into buffer at first, instead of writing directly into the file
                # This enables for example the generation of table of contents
                filename="example.md", enable_write=False
        ) as doc:
            doc.addHeader(1, "Hello there!")
            doc.writeTextLine(f'{doc.addBoldedText("This is just a test.")}')
            doc.addHeader(2, "Second level header.")
            table = [
                {"Column1": "col1row1 data", "Column2": "col2row1 data"},
                {"Column1": "col1row2 data", "Column2": "col2row2 data"},
            ]

            doc.addTable(dictionary_list=table)
            print(doc)
            doc.writeTextLine("Ending the document....")

