from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session
from src.services.UserServices import register_user, select_user, get_user_by_id, verify_password
import functools

auth = Blueprint('auth', __name__, url_prefix='/auth')

# User register
@auth.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
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
                return redirect(url_for("home.homef"))
            else:
                flash("El usuario ya está registrado. Por favor, elige otro nombre de usuario.", 'error')
                return render_template("auth/register.html", error=error)
            
    return render_template("auth/register.html", error=error)


# User login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        if not username:
            error = 'Se requiere completar el campo Nombre de usuario'
        elif not password:
            error = 'Se requiere completar el campo Contraseña'
        else:
            user_exist = select_user(username)

            if user_exist is None or not verify_password(user_exist[4], password):
                flash("Usuario y/o contraseña incorrecta.", 'error')
                return render_template("auth/login.html", error=error)
            else:
                session.clear()
                session['user_id'] = user_exist[0]
                return redirect(url_for("home.homef"))
                          
    return render_template("auth/login.html", error=error)


# Logged User
@auth.before_app_request
def logged_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_user_by_id(user_id)


# Logout
@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index.indexf'))


# Login required
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
