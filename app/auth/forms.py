# -*- coding:utf-8 -*-  
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
        Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Log In')

class RegistrationForm(Form):
    email = StringField('Email', validators = [Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

