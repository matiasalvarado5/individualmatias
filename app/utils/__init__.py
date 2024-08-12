from flask import url_for, redirect, g, session
import functools

def login_required_user(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

def logout_user():
    session.clear()
    return redirect(url_for('index.index'))
