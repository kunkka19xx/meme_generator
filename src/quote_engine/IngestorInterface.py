"""Ingestor Interface."""

from abc import ABC, abstractmethod
from typing import List

from models import QuoteModel


class IngestorInterface(ABC):
    """Use Abstract Base Classes (ABC) in Python and implement this design pattern."""

    can_ingest_extensions = []
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Implement to verify if the file type is compatible with the ingestor class.
        
        :param path: 
        :return: 
        """
        if path.split('.')[-1] in cls.can_ingest_extensions:
            return True
        else:
            return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Implement to parse the file content and output into QuoteModel object.

        :param path:
        :return:
        """
        pass