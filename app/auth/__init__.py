from flask import Blueprint, current_app
from flask.ext.login import logout_user, login_required, current_user, login_user
auth = Blueprint('auth', __name__)

from . import views

@auth.app_context_processor
def inject_configuration():
    if current_app.user:
        return dict(email=current_app.user.email,blogname=current_app.user.blogname, background=current_app.user.background, head_image=current_app.user.head_image, tags = current_app.user.tags )
    return dict(head_image=current_app.config['DEFAULT_HEAD_IMAGE'], blogname=current_app.config['DEFAULT_NAME'],  background=current_app.config['DEFAULT_BACKGROUND'])
