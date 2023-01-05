"""TextIngestor module."""

from typing import List
from models import QuoteModel
import logging as log
from quote_engine import IngestorInterface


class TextIngestor(IngestorInterface):
    """
    The class inherits the IngestorInterface.

    The class does not depend on any 3rd party library to complete the defined, abstract method signatures to parse Text files.
    """

    can_ingest_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Implement to parse the text file content and output into QuoteModel object.

        :param path:
        :return:
        """
        result = []
        if cls.can_ingest(path) is False:
            log.exception("File is not text type!")
            return

        try:
            with open(path, mode='r') as file:
                while True:
                    content = file.readline().strip(' ').strip('\n\r')
                    if not content:
                        break
                    else:
                        # Read data line by line and store body & author into array
                        data = content.strip('\n\r').split(' - ')
                    result.append(
                        QuoteModel(
                            body=data[0].strip(' ').strip('\n\r').strip(),
                            author=data[1].strip(' ').strip('\n\r').strip()
                        )
                    )
        except Exception as exception:
            log.error("An error occurred while parsing the file!")
            log.exception(exception)
        return result






