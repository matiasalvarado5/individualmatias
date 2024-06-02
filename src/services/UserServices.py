from werkzeug.security import generate_password_hash, check_password_hash
from src.database import db, cursor

def select_user(username):
    cursor.execute("SELECT * FROM users WHERE username = (%s)", (username,))
    return cursor.fetchone()

def register_user(name, surname, username, password):
    hashed_password = generate_password_hash(password)
    cursor.execute("INSERT INTO users (id, name, surname, username, password) VALUES (id, %s, %s, %s, %s)", (name, surname, username, hashed_password))
    db.commit()

def get_user_by_id(user_id):
    cursor.execute("SELECT * FROM users WHERE id = (%s)", (user_id,))
    return cursor.fetchone()

def verify_password(password, hashed_password):
    return check_password_hash(password, hashed_password)
