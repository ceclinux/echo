# -*- coding:utf-8 -*-  
import os
import logging
from logging.handlers import SMTPHandler
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'Life is so hard'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    ECHO_MAIL_SUBJECT_PREFIX = '[Echo]'
    ECHO_MAIL_SENDER = 'zhengzihuiecho@126.com'
    MAIL_SERVER = 'smtp.126.com'
    ECHO_ADMIN = 'src655@gmail.com'
    MAIL_USERNAME = 'zhengzihuiecho'
    MAIL_PASSWORD = 'tbfkcvocrkvfhggy'
    DEFAULT_BACKGROUND = 'http://img.vim-cn.com/5a/0afa5a08d5bc65a8be7232a49d699fe33cad58.jpg'
    DEFAULT_HEAD_IMAGE = 'http://img.vim-cn.com/d9/43603e57e56daeda2811d66bd5c42de098dd7b.png'
    DEFAULT_NAME = '无名氏'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    SSL_DISABLE = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    Debug = True
    DATABASE_URI = os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'data.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

class HerokuConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)
        # 输出到 stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler)
        SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)
   
config = {
        'developement' : DevelopmentConfig, 
        'testing':TestingConfig, 
        'production':ProductionConfig, 
        'default': DevelopmentConfig
        }

