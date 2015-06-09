# -*- coding:utf-8 -*-  
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Length, URL
from wtforms.fields import Field

class EditProfileForm(Form):
    blogname = StringField('你给你的博客取什么名字', validators=[Length(0, 64)])
    head_image = StringField('头像的URL', validators=[URL(message="这不是合格的URL哦")])
    background = StringField('背景图片', validators=[URL(message="这不是合格的URL哦")])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')

class PostForm(Form):
    title = StringField('标题')
    postcontent = TextAreaField('写点什么把')
    tagsinput = StringField('标签')
    submit = SubmitField('提交')
