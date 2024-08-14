# MODULES
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String
from app.models.users import User
from flask import redirect, url_for, session, g
import functools
from app.database.connection import get_db_connection

# VARIABLES
db_session, engine = get_db_connection()

# FUNCTIONS
def register_user(name, surname, username, password,id_rol):
    hashed_password = generate_password_hash(password)
    new_user = User(name=name, surname=surname, username=username, password=hashed_password,id_rol=id_rol)
    db_session.add(new_user)
    db_session.commit()
    db_session.close()

def select_user(username):
    user_selected = db_session.query(User).filter_by(username=username).first()
    db_session.close()
    return user_selected

def get_user_by_id(user_id):
    user_selected = db_session.query(User).filter_by(id=user_id).first()
    db_session.close()
    return user_selected

def select_all_users():
    users = db_session.query(User).all()
    db_session.close()
    return users

def update_user(user_id, new_name=None, new_surname=None, new_username=None, new_password=None):
    user_to_update = get_user_by_id(user_id)
    user_to_update.name = new_name
    user_to_update.surname = new_surname
    user_to_update.username = new_username
    user_to_update.password = new_password
    db_session.add(user_to_update)
    db_session.commit()
    db_session.close()


def delete_user(user_id):
    user_to_delete = get_user_by_id(user_id)
    db_session.delete(user_to_delete)
    db_session.commit()
    db_session.close()