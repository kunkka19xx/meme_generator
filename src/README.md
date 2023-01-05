<h1>Project: Meme Generator</h1>

<h3>Overview</h3>
<p>The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. It’s not that simple though! Your content team spent countless hours writing quotes in a variety of filetypes. You could manually copy and paste these quotes into one standard format – but you’re going to over-engineer a solution to load quotes from each file to show off your fancy new Python skills.</p>
<h4>Using:</h4> 
    - Pillow
    <br>
    - Pandas
    <br>
    - XPdf
    <br>
    - python-docx
    <br>
    - flask

    

<h3>Instruction</h3>

- CLI:
> $ python main.py --help
> usage: main.py [-h] [-p PATH] [-b BODY] [-a AUTHOR]
- Arguments:
> -p: Path to image
<br>
> -body: Text content for meme
<br>
> -author: Author of meme

- Web application:
> python app.py

<h3>Modules</h3>
- QuoteEngine module: 
<p>
The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:
Example:

"This is a quote body" - Author

This module will be composed of many classes and will demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.
</p>

- MemeEngine module:

<br>
<p>
The Meme Engine Module is responsible for manipulating and drawing text onto images. It will reinforce your understanding of object-oriented thinking while demonstrating your skill using a more advanced third party library for image manipulation.
</p>

- Model module:

<p>
This module contains models such as QuoteModel object, which contains text fields for body and author. The class overrides the correct methods to instantiate the class and print the model contents as: ”body text” - author
</p>

