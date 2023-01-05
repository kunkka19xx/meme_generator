"""This accepts an image output path, selects,saves a random image and quote."""

import random
import textwrap

from PIL import Image, ImageDraw
from datetime import datetime
import logging as log


class MemeEngine:
    """
    This class takes in an image output path.

    selects a random image and quote,
    Saves the image to the output path and returns the path to the image.
    """

    def __init__(self, path):
        """Create instance of class."""
        self.path = path

    def make_meme(self, path, text, author, width=500) -> str:
        """Create meme with provided text and author."""
        try:
            img = Image.open(path)
        except Exception as ex:
            log.exception("Exception while opening file: " + ex)
        else:
            if width is not None:
                ratio = width / float(img.size[0])
                height = int(ratio * float(img.size[1]))
                img = img.resize((int(width), int(height)), Image.NEAREST)

            if text != "" and author != '':
                body = f'{text}\n- {author}'
                draw = ImageDraw.Draw(img)
                img_width = img.width
                img_height = img.height
                x_axis = random.randint(10, int(img_width/3))
                y_axis = random.randint(10, img_height - 40)
                body = body.replace(u'\u2019', "'").replace(u'\ufeff', '')

                wrapper = textwrap.TextWrapper(width=50)
                word_list = wrapper.wrap(text=body)

                draw.text((x_axis, y_axis), word_list)

            now = datetime.utcnow()
            dt_string = now.strftime("%d%m%Y_%H_%M_%S_%f")
            path = f'{self.path}/img_{dt_string}.jpeg'

            img.save(path)
            print(f"Meme saved to {self.path}")
            return path