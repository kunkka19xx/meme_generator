"""PDFIngestor module."""

import os
from datetime import datetime
import subprocess
from typing import List
from models import QuoteModel
import logging as log
from quote_engine import IngestorInterface
from quote_engine import TextIngestor

class PDFIngestor(IngestorInterface):
    """
    The class inherits the IngestorInterface.

    The PDFIngestor class utilizes the subprocess module to call the pdftotext CLI.
    """

    can_ingest_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Implement to parse the pdf file content and output into QuoteModel object.

        :param path:
        :return:
        """
        if cls.can_ingest(path) is False:
            log.exception("File is not docx type!")
            return

        now = datetime.utcnow()
        dt_string = now.strftime("%d%m%Y_%H_%M_%S_%f")
        temp_dir = f'./temporary/{dt_string}.txt'
        args = ['pdftotext', path, temp_dir]
        try:
            subprocess.call(args)
            return TextIngestor.parse(temp_dir)
        except Exception as exception:
            log.error("An error occurred while parsing the file!")
            log.exception(exception)
        finally:
            os.remove(temp_dir)







