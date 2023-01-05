"""This is the main app to be served via flask."""

import random
import os
import requests
from flask import Flask, render_template, request
from quote_engine import Ingestor
from meme_engine import MemeEngine
import logging as log
from datetime import datetime

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the quote_files variable
    quotes = []

    for file in quote_files:
        quote = Ingestor.parse(file)
        if quote is not None:
            quotes.append(quote)

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all images within the images images_path directory
    imgs = []

    for file in os.listdir(images_path):
        if file.endswith(".jpg"):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()


def make_default_info():
    """Make default path."""
    path = meme.make_meme('./_data/photos/dog/xander_1.jpg', 'This is body', 'Author')
    return path


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(random.choice(quotes))

    if quote and img:
        path = meme.make_meme(img, quote.body, quote.author)
        return render_template('meme.html', path=path)
    else:
        path = make_default_info()
        return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    try:
        img = requests.get(image_url)
    except Exception as err:
        log.exception(f'Cannot access the url. Please verify that is a correct url!'
                      f'Detail: {err}')
        return render_template('err.html', path='')

    path = None
    now = datetime.utcnow()
    dt_string = now.strftime("%d%m%Y_%H_%M_%S_%f")
    try:

        temp_img = f'temporary/{dt_string}.jpg'
        open(temp_img, 'wb').write(img.content)
    except:
        log.exception("Cannot open image!")
        path = make_default_info()
    else:
        path = meme.make_meme(temp_img, body, author)
        os.remove(temp_img)
    finally:
        return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
