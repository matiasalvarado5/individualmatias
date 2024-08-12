from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session, jsonify, current_app
from app.services.UserServices import register_user, select_user, get_user_by_id, verify_password,logged_user,login_required_user,logout_user
import functools
import jwt
import datetime



auth = Blueprint('auth', __name__, url_prefix='/auth')

# User register
@auth.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            name = data.get("name")
            surname = data.get("surname")
            username = data.get("username")
            password = data.get("password")
            id_rol = data.get("id_rol")
        else:
            name = request.form["name"]
            surname = request.form["surname"]
            username = request.form["username"]
            password = request.form["password"]
            id_rol = request.form["id_rol"]

        if not name:
            error = 'Se requiere completar el campo Nombre'
        elif not surname:
            error = 'Se requiere completar el campo Apellido'
        elif not username:
            error = 'Se requiere completar el campo Nombre de usuario'
        elif not password:
            error = 'Se requiere completar el campo Contraseña'
        else:
            if select_user(username) is None:
                register_user(name, surname, username, password,id_rol)
                print("Usario registrado correctamente")
                return jsonify({"message":"Usuario registrado correctamente","name":name,"surname":surname,"username":username})
            else:
                print("El usuario ya esta registrado")
                return jsonify({"message":"El nombre de usuario ya se encuentra registrado","name":name, "surname":surname, "username":username})
            
    return "Pagina de registro"

# User login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    token = None
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")
        else:
            username = request.form["username"]
            password = request.form["password"]

        if not username:
            error = 'Se requiere completar el campo Nombre de usuario'
        elif not password:
            error = 'Se requiere completar el campo Contraseña'
        else:
            user_exist = select_user(username)

            if user_exist is None or not verify_password(password,user_exist.password):
                flash("Usuario y/o contraseña incorrecta.")
                print("Usuario y/o contraseña incorrecta")
                return render_template("auth/login.html", error=error)
            else:
                if user_exist.id_rol == 1:
                    session.clear()
                    session['user_id'] = user_exist.id
                    token = jwt.encode({
                        'sub': username,
                        'role': user_exist.id_rol,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=0.25)  # Token válido por 1 hora}
                    },current_app.config['SECRET_KEY'], algorithm="HS256")
                    print("Inicio de sesion de admin")
                    return jsonify({"message":"Bienvenido admin","id":user_exist.id,"name":user_exist.name,"surname":user_exist.surname,"username":user_exist.username,"id_rol":user_exist.id_rol,"token":token})
                elif user_exist.id_rol == 2:
                    session.clear()
                    session['user_id'] = user_exist.id
                    token = jwt.encode({
                        'sub': username,
                        'role':user_exist.id_rol,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=0.25)  # Token válido por 1 hora}
                    },current_app.config['SECRET_KEY'], algorithm="HS256")
                    print("Inicio de sesion de admin")
                    print("Inicio de sesion usuario")
                    return jsonify({"message":"Bienvenido usuario","id":user_exist.id,"name":user_exist.name,"surname":user_exist.surname,"username":user_exist.username,"token":token})
    return render_template("auth/login.html", error=error)


# Logged User
@auth.before_app_request
def logged():
    logged_user()

# Logout
@auth.route("/logout")
def logout():
    return logout_user()

