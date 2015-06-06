from flask import render_template, redirect, request, url_for, flash, current_app, g
from flask.ext.login import logout_user, login_required, current_user, login_user
from . import auth
from .. import db, User
from .forms import LoginForm, RegistrationForm
from ..decorators import *
import re

@auth.route('/login', methods=['GET', 'POST'])
@has_not_user_registered
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, True)
            return redirect(url_for('main.index'))
        flash('邮箱或者密码输错啦')
    return render_template('auth/registerandlogin.html', form=form, header="登录")


@auth.route('/register', methods=['GET', 'POST'])
@has_user_registered
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,  password=form.password.data, head_image = current_app.config['DEFAULT_HEAD_IMAGE'],background = current_app.config['DEFAULT_BACKGROUND'], blogname = re.sub(r'@.*', '', form.email.data), about_me = "")
        db.session.add(user)
        db.session.commit()
        current_app.user = User.query.get(1)
        flash('注册成功～\(^o^)/~')
        return redirect(url_for('main.index'))
    return render_template('auth/registerandlogin.html', form=form, header="注册")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经登出啦')
    return redirect(url_for('main.index'))

