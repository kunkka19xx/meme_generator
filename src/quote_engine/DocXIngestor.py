"""DocXIngestor Module."""

from typing import List
import docx
from models import QuoteModel
import logging as log
from quote_engine import IngestorInterface


class DocXIngestor(IngestorInterface):
    """
    The class inherits the IngestorInterface.

    The class depends on the python-docx library to complete the defined, abstract method signatures to parse DOCX files.
    """

    can_ingest_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Implement to parse the docx file content and output into QuoteModel object.

        :param path:
        :return:
        """
        result = []
        if cls.can_ingest(path) is False:
            log.exception("File is not docx type!")
            return

        try:
            doc = docx.Document(path)
            for line in doc.paragraphs:
                if len(line.text) == 0:
                    continue
                # Read data line by line and store body & author into array
                data = line.text.strip('\n\r').split(' - ')
                body = data[0].strip(' ')
                result.append(
                    QuoteModel(
                        body=body,
                        author=data[1]
                    )
                )
        except Exception as exception:
            log.error("An error occurred while parsing the file!")
            log.exception(exception)
        return result







