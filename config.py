import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'Life is so hard'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Echo]'
    ECHO_MAIL_SENDER = 'Ruochen Shen <src655@gmail.com>'
    DEFAULT_BACKGROUND = 'http://img.vim-cn.com/5a/0afa5a08d5bc65a8be7232a49d699fe33cad58.jpg'
    DEFAULT_HEAD_IMAGE = 'http://img.vim-cn.com/d9/43603e57e56daeda2811d66bd5c42de098dd7b.png'
    DEFAULT_NAME = '无名氏'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    Debug = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    #MAIL_USE_TLS = True
    MAIL_USERNAME = 'zhengzihuiecho@126.com'
    MAIL_PASSWORD = 'echozhengzihui'
    DATABASE_URI = os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'data.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConifg(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
        'developement' : DevelopmentConfig, 
        'testing':TestingConfig, 
        'production':ProductionConifg, 
        'default': DevelopmentConfig
        }
