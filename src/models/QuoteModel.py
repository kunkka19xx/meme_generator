"""A simple QuoteModel class to encapsulate the body and author."""


class QuoteModel:
    """A simple QuoteModel class to encapsulate the body and author."""

    def __init__(self, body, author):
        """
        Initialize of QuoteModel.

        :param body:
        :param author:
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Override the __str__ or __repr__ method to print the model contents as "body text" - author"""
        return f'"{self.body}" - {self.author}'