"""This is a subclass of IngestorInterface for parsing file."""

from typing import List
from models.QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocXIngestor import DocXIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """All ingestors are packaged into this Ingestor class."""

    all_ingestors = [DocXIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Class method to parse content file to QuoteModel.

        :param path:
        :return:
        """
        for ingestor in cls.all_ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
