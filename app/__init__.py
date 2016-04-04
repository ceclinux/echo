# -*- coding:utf-8 -*-  
from flask.ext.pagedown import PageDown
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin, AnonymousUserMixin
from flask import Flask, render_template, session, current_app, g
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config
from datetime import datetime

login_manager = LoginManager()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy(session_options={'expire_on_commit': False})
pagedown = PageDown()


class MyServer(Flask):

    def __init__(self, *args, **kwargs):
            super(MyServer, self).__init__(*args, **kwargs)

            #instanciate your variables here
            self.user = None


def create_app(config_name):
    app = MyServer(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    login_manager.login_view="auth.login"
    login_manager.login_message="先要登录才能看哦"
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    pagedown.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    @app.before_first_request
    def def_user(*args, **kwargs):
        current_app.user = User.query.get(1)
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask.ext.sslify import SSLify
        sslify = SSLify(app)
    return app

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    head_image = db.Column(db.String(128))
    background = db.Column(db.String(128))
    blogname = db.Column(db.String(128))
    about_me = db.Column(db.String(1024))
    tags = db.Column(db.String(1024))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text)
    #body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index = True, default=datetime.utcnow)
    tags = db.Column(db.String(128))
    title = db.Column(db.String(128))
    hide = db.Column(db.Boolean)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
