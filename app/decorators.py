from functools import wraps
from flask import current_app, flash, redirect, url_for

def has_not_user_registered(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_app.user:
            flash('还没注册过呢～')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

def has_user_registered(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_app.user:
            flash('已经注册过啦～')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function
