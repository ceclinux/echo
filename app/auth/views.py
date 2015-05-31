from flask import render_template, redirect, request, url_for, flash, current_app, g
from flask.ext.login import login_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm
from ..decorators import *

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/registerandlogin.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
@has_user_registered
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data, head_image = current_app.config['DEFAULT_HEAD_IMAGE'],background = current_app.config['DEFAULT_BACKGROUND'], blogname = form.username.data +" 's Blog")
        db.session.add(user)
        db.session.commit()
        current_app.has_user=True
        flash('Congratulations!You has been registed')
        return redirect(url_for('main.index'))
    return render_template('auth/registerandlogin.html', form=form)
