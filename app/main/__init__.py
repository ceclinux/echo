from flask import Blueprint, current_app
from flask.ext.login import logout_user, login_required, current_user, login_user

main = Blueprint('main', __name__)
from . import views

@main.app_context_processor
def inject_configuration():
    if not current_app.user:
        return dict(head_image=current_app.config['DEFAULT_HEAD_IMAGE'], blogname=current_app.config['DEFAULT_NAME'],  background=current_app.config['DEFAULT_BACKGROUND'])
    if current_app.user:
        return dict(email=current_app.user.email,blogname=current_app.user.blogname, background=current_app.user.background, head_image=current_app.user.head_image, about_me =current_app.user.about_me)
    return dict()
