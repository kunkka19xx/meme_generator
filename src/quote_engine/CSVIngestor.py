"""CSVIngestor module."""

from typing import List
from models import QuoteModel
import logging as log
from quote_engine import IngestorInterface
import pandas as pd


class CSVIngestor(IngestorInterface):
    """
    The class inherits the IngestorInterface.

    The class depends on the pandas library to complete the defined, abstract method signatures to parse CSV files.
    """

    can_ingest_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Implement to parse the csv file content and output into QuoteModel object.

        :param path:
        :return:
        """
        result = []
        if cls.can_ingest(path) is False:
            log.exception("File is not docx type!")
            return

        try:
            df = pd.read_csv(path)
            for i in range(len(df)):
                result.append(
                    QuoteModel(
                        body=df["body"][i],
                        author=df["author"][i],
                    )
                )
        except Exception as exception:
            log.error("An error occurred while parsing the file!")
            log.exception(exception)
        return result






