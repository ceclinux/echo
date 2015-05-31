import markdown
from flask import render_template, current_app, request, g
from . import main


@main.route('/')
def index():
    text = ""
    body=markdown.markdown(text, extensions=['markdown.extensions.nl2br', 'markdown.extensions.tables'])
    return render_template('index.html',mardown = markdown , email="src655@gmail.com")
