import markdown
from flask import render_template, current_app, request
from . import main


@main.route('/')
def index():
    text = ""
    body=markdown.markdown(text, extensions=['markdown.extensions.nl2br', 'markdown.extensions.tables'])
    return render_template('index.html',mardown = markdown , email=current_app.user['email'],blogname=current_app.user['blogname'], background=current_app.user['background'], head_image=current_app.user['head_image'] )
