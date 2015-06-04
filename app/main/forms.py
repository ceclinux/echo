from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Length, URL

class EditProfileForm(Form):
    blogname = StringField('你给你的博客取什么名字', validators=[Length(0, 64)])
    head_image = StringField('头像的URL', validators=[URL(message="这不是合格的URL哦")])
    background = StringField('背景图片', validators=[URL(message="这不是合格的URL哦")])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')


