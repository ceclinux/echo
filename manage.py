# -*- coding:utf-8 -*-  
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from app import create_app, db, User, Post
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app('heroku')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)

manager.add_command('shell', Shell(make_context = make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def deploy():
    """Run deployment tasks."""
    from flask.ext.migrate import upgrade
    upgrade()

@manager.command
def init():
    """Run deployment tasks."""
    db.create_all()

if __name__ == '__main__':
    manager.run()
