# -*- coding:utf-8 -*-  
import os
from app import create_app, db, User, Post
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app('heroku')
app.debug=True
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)

manager.add_command('shell', Shell(make_context = make_shell_context))
manager.add_command('db', MigrateCommand)
port=int(os.environ.get('PORT',  5000))
manager.add_command('runserver', Server(port=port, host="0.0.0.0"))

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
