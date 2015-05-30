from flask import Blueprint, current_app

main = Blueprint('main', __name__)
from . import views

@main.app_context_processor
def inject_configuration():
    return dict(head_image=current_app.config['DEFAULT_HEAD_IMAGE'], blogname=current_app.config['DEFAULT_NAME'],  background=current_app.config['DEFAULT_BACKGROUND'])
