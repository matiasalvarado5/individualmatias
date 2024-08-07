from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session
from src.services.UserServices import register_user, select_user, get_user_by_id, verify_password,logged_user,login_required_user,logout_user
import functools

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
        else:
            name = request.form["name"]
            surname = request.form["surname"]
            username = request.form["username"]
            password = request.form["password"]

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
                register_user(name, surname, username, password)
                print("Usario registrado correctamente")
                return redirect(url_for("home.homef"))
            else:
                flash("El usuario ya está registrado. Por favor, elige otro nombre de usuario.", 'error')
                print("El usuario ya esta registrado")
                return render_template("auth/register.html", error=error)
            
    return render_template("auth/register.html", error=error)


# User login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
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
                session.clear()
                session['user_id'] = user_exist.id
                print("Inicio de sesion correcto")
                return redirect(url_for("home.homef"))
                          
    return render_template("auth/login.html", error=error)


# Logged User
@auth.before_app_request
def logged():
    logged_user()

# Logout
@auth.route("/logout")
def logout():
    return logout_user()

