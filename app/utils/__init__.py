from flask import url_for, redirect, g, session,current_app, jsonify,request
import functools
from functools import wraps
import jwt
import datetime
from werkzeug.security import check_password_hash,generate_password_hash
from app.services.UserServices import select_user,get_user_by_id


def generate_token(username,id_rol,):
    token = jwt.encode({
                        'sub': username,
                        'role': id_rol,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
                    },current_app.config['SECRET_KEY'], algorithm="HS256")
    return token


def verify_password(password, hashed_password):
    return check_password_hash(hashed_password, password)


def login_required_user(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


def logout_user():
    session.clear()
    return "Sesion finalizada"

def logged_user():
    user_id = session.get('id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_user_by_id(user_id)


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({"message": "Token no proporcionado"}), 403
        
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            if data['role'] != 1:
                return jsonify({"message": "No tienes permiso para realizar esta accion"}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token ha expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token invalido"}), 401

        return f(*args, **kwargs)
    return decorated_function


def token_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Buscar el token en el encabezado de la solicitud
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        
        if not token:
            return jsonify({"message": "Token es requerido"}), 401
        
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            g.user = select_user(data['sub'])  # Obtén el usuario basado en el contenido del token
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token invalido"}), 401

        return f(*args, **kwargs)
    
    return decorated
