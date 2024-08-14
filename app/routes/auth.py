# app/routes/auth.py
from flask import Blueprint, request, jsonify, session, redirect, url_for, g, current_app
from app.services.UserServices import register_user, select_user, get_user_by_id
from app.utils import token_required, admin_required, generate_token, logout_user, logged_user
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

auth = Blueprint('auth', __name__, url_prefix='/auth')


# User register
@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get("name")
        surname = data.get("surname")
        username = data.get("username")
        password = data.get("password")
        id_rol = data.get("id_rol", 2)  # Default role is 2

        if not all([name, surname, username, password]):
            return jsonify({"message": "Todos los campos son requeridos"}), 400
        if select_user(username):
            return jsonify({"message": "El nombre de usuario ya se encuentra registrado"}), 400
        register_user(name, surname, username, password, id_rol)
        return jsonify({"message": "Usuario registrado correctamente"}), 201

    elif request.method == 'GET':
        return jsonify({'Message':"Pagina de registro"})


# User login
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        user = select_user(username)
        if not all([username, password]):
            return jsonify({"message": "Nombre de usuario y contraseña son requeridos"}), 400
        user = select_user(username)
        if user is None or not check_password_hash(user.password, password):
            return jsonify({"message": "Usuario y/o contraseña incorrecta"}), 401
        token = generate_token(username,user.id_rol)
        return jsonify({"message":"Inicio de sesion correcto","name":user.name,"surname":user.surname,"username":username,"token": token}), 200
    
    elif request.method == 'GET':
        return jsonify({"Message":"Pagina de inicio de sesion"})


# Logout
@auth.route('/logout', methods=['POST'])
@token_required
def logout():
    session.clear()
    return ("Sesion Finalizada")


# Logged User
@auth.before_app_request
def logged():
    logged_user()

