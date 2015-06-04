import markdown
from flask import render_template, current_app, request, flash, redirect, url_for
from flask.ext.login import logout_user, login_required, current_user
from . import main
from .forms import EditProfileForm
from .. import db, User


@main.route('/')
def index():
    text = ""
    body=markdown.markdown(text, extensions=['markdown.extensions.nl2br', 'markdown.extensions.tables'])
    return render_template('index.html', markdown = markdown)


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
