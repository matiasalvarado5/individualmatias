# MODULES
from app.models.post import Post
from flask import redirect, url_for, session, g
import functools
from app.database.connection import get_db_connection
from datetime import datetime


# VARIABLES
db_session, engine = get_db_connection()

# FUNCTIONS
def add_post(author, title, body, date):
    new_post = Post(author=author, title=title, body=body)
    db_session.add(new_post)
    db_session.commit()
    db_session.close()
    return new_post

def select_post(title):
    post_selected = db_session.query(Post).filter_by(title=title).first()
    db_session.close()
    return post_selected

def get_post_by_id(post_id):
    post_selected = db_session.query(Post).filter_by(id=post_id).first()
    db_session.close()
    return post_selected

def select_all_post():
    posts = db_session.query(Post).all()
    db_session.close()
    return posts

def update_post(post_id, new_title=None, new_body=None):
    post_to_update = get_post_by_id(post_id)
    post_to_update.title = new_title
    post_to_update.body = new_body
    post_to_update.date = datetime.utcnow()
    db_session.add(post_to_update)
    db_session.commit()
    db_session.close()

def delete_post(id):
    post_to_delete = get_post_by_id(id)
    if not post_to_delete:
        return "No se puede eliminar el post",404
    else:
        db_session.delete(post_to_delete)
        db_session.commit()
        db_session.close()