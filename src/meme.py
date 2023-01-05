"""meme generator."""

import os
import random
import argparse
from meme_engine import MemeEngine
from quote_engine import Ingestor
from models import QuoteModel
import logging as log


def generate_meme(path=None, body=None, author=None):
    """
    Generate a meme given an path and a quote.

    :param path:
    :param body:
    :param author:
    :return:
    """
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img_path = random.choice(imgs)
    else:
        img_path = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            log.error("If body is existed, author is required!")
            return
        if body is None:
            log.error("If author is existed, body is required!")
            return
        quote = QuoteModel(body, author)

    meme = MemeEngine('./static')
    path = meme.make_meme(img_path, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    args_parser = argparse.ArgumentParser(description="Welcome to Meme Generator.")
    args_parser.add_argument('--path', type=str, default=None, help="Path to an image file.")
    args_parser.add_argument('--body', type=str, default=None, help="Quote body to add to the image.")
    args_parser.add_argument('--author', type=str, default=None, help="Quote author to add to the image.")
    args = args_parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))