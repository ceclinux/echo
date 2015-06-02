import markdown
from flask import render_template, current_app, request
from . import main


@main.route('/')
def index():
    print("current_app.user")
    print(current_app.user)
    text = ""
    body=markdown.markdown(text, extensions=['markdown.extensions.nl2br', 'markdown.extensions.tables'])
    if current_app.user:
        return render_template('index.html',markdown = markdown , email=current_app.user.email,blogname=current_app.user.blogname, background=current_app.user.background, head_image=current_app.user.head_image )
    return render_template('index.html')
