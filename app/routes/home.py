from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session, jsonify
from src.services.UserServices import login_required_user,logged_user,select_all_users,get_user_by_id,update_user
from werkzeug.security import generate_password_hash

home = Blueprint('home', __name__,url_prefix='/home')

@login_required_user
@home.route("/")
def homef():
    return "Inicio para logueados"

@login_required_user
@home.route('/users', methods=['GET'])
def home_get_users():
        users = select_all_users()
        lista_users = []
        for user in users:
            lista_users.append({"id":user.id,
                    "id_rol":user.id_rol,
                    "name":user.name,
                    "surname":user.surname,
                    "username":user.username})
        return lista_users

@login_required_user
@home.route("/users/<int:id>",methods=['GET','PUT'])
def home_get_user(id):
    if request.method == 'PUT':
        user = get_user_by_id(id)
        data = request.get_json()
        name = data.get("name")
        surname = data.get("surname")
        username = data.get("username")
        password = data.get("name")
        if not user:
            return "No existe el usuario"
        else:
            update_user(id,name,surname,username,password)
            new_password = generate_password_hash(password)
            
            return jsonify({"message":"Usuario actualizado correctamente","name":name,"surname":surname,"username":username,"password":new_password})
    
    else:
        user = get_user_by_id(id)
        if not user:
            return"No existe el usuario"
        return jsonify({"id":user.id,"name":user.name,"surname":user.surname,"username":user.username})

