from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Length, URL
from wtforms.fields import Field
from wtforms.widgets import TextInput

class TagListField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else: return u'' 
    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []

class BetterTagListField(TagListField):
    def __init__(self, label='', validators=None, remove_duplicates=True, **kwargs):
        super(BetterTagListField, self).__init__(label, validators, **kwargs)
        self.remove_duplicates = remove_duplicates

    def process_formdata(self, valuelist):
        super(BetterTagListField, self).process_formdata(valuelist)
        if self.remove_duplicates:
            self.data = list(self._remove_duplicates(self.data))

    @classmethod
    def _remove_duplicates(cls, seq):
        """Remove duplicates in a case insensitive, but case preserving manner"""
        d = {}
        for item in seq:
            if item.lower() not in d:
                d[item.lower()] = True
                yield item

class EditProfileForm(Form):
    blogname = StringField('你给你的博客取什么名字', validators=[Length(0, 64)])
    head_image = StringField('头像的URL', validators=[URL(message="这不是合格的URL哦")])
    background = StringField('背景图片', validators=[URL(message="这不是合格的URL哦")])
    about_me = TextAreaField('关于我')
    submit = SubmitField('提交')

class PostForm(Form):
    postcontent = TextAreaField('写点什么把')
    tagsinput = StringField('tags')
    submit = SubmitField('提交')


