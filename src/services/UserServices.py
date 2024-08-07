# MODULES
from werkzeug.security import generate_password_hash, check_password_hash
from src.utils import login_required_user, logout_user
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from src.models.users import User
from flask import redirect, url_for, session, g
import functools
from src.database.connection import get_db_connection

# VARIABLES
db_session, engine = get_db_connection()

# FUNCTIONS
def select_user(username):
    user_selected = db_session.query(User).filter_by(username=username).first()
    db_session.close()
    return user_selected

def register_user(name, surname, username, password):
    hashed_password = generate_password_hash(password)
    new_user = User(name=name, surname=surname, username=username, password=hashed_password)
    db_session.add(new_user)
    db_session.commit()
    db_session.close()

def get_user_by_id(user_id):
    user_selected = session.query(User).filter_by(id=user_id).first()
    db_session.close()
    return user_selected

def verify_password(password, hashed_password):
    return check_password_hash(hashed_password, password)

def logged_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_user_by_id(user_id)

def logout_user():
    session.clear()
    return redirect(url_for('index.index'))
