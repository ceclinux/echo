from flask.ext.pagedown import PageDown
from flask import Flask, render_template, session, current_app, g
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config
import sqlite3

login_manager = LoginManager()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
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
        g.db = sqlite3.connect(current_app.config['DATABASE_URI'])
        current_app.user = query_db('select * from user')
    return app

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv
