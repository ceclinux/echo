import markdown
from flask import render_template, current_app, request, flash, redirect, url_for
from flask.ext.login import logout_user, login_required, current_user
from . import main
from .forms import EditProfileForm, PostForm
from .. import db, User, Post
import sqlite3


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditProfileForm()
    if form.validate_on_submit():
        User.query.filter_by(id=1).update(dict(blogname = form.blogname.data, head_image = form.head_image.data, background=form.background.data, about_me = form.about_me.data))
        db.session.commit()
        current_app.user = User.query.get(1)
        flash('你的个人资料已经更新~\(≧▽≦)/~')
        return redirect(url_for('.index'))
    form.blogname.data = current_app.user.blogname
    form.head_image.data = current_app.user.head_image
    form.background.data = current_app.user.background
    form.about_me.data = current_app.user.about_me
    return render_template('edit_profile.html', form = form, header="设置")


@main.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.postcontent.data, tags = form.tagsinput.data, title = form.tagsinput.data)
        db.session.add(post)
        db.session.commit()
        print(form.tagsinput.data)
        print(type(form.tagsinput.data))
        if not current_app.user.tags:
            User.query.filter_by(id=1).update(dict(tags = form.tagsinput.data))
            current_app.user = User.query.get(1)
        tagsdiff = set(form.tagsinput.data.split(','))-set(current_app.user.tags.split(','))
        if tagsdiff:
            User.query.filter_by(id=1).update(dict(tags = current_app.user.tags +','+ ','.join(set(tagsdiff))))
            current_app.user = User.query.get(1)
        flash('文章发出成功！')
        return redirect(url_for('.p', id=post.id))
    return render_template('post.html', form = form)


@main.route('/p/<int:id>', methods=['GET'])
def p(id):
    post = Post.query.get_or_404(id)
    body=markdown.markdown(post.body, extensions=['markdown.extensions.nl2br', 'markdown.extensions.tables'])
    return render_template('index.html', body = body, title=post.title, tags=post.tags)

@main.route('/tag/<tagname>')
def tag(tagname):
    post = Post.query.filter(Post.tags.like('%'+tagname+'%')).order_by(Post.timestamp.desc())
    return render_template('tags.html', post=post)
