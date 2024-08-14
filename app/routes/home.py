# app/routes/home.py
from flask import Blueprint, request, jsonify, g
from app.services.UserServices import select_all_users, get_user_by_id, update_user, delete_user
from app.utils import token_required, admin_required, logged_user,login_required_user
from app.services.PostServices import add_post, select_post,select_all_post,get_post_by_id,delete_post,update_post
from datetime import datetime
home = Blueprint('home', __name__, url_prefix='/home')


@home.route('/post',methods=['GET'])
@token_required
@login_required_user
def inicio():
    posts = select_all_post()
    lista_post = [{"id":post.id,"author":post.author,"title":post.title,"body":post.body,"date":post.date} for post in posts]
    return jsonify(lista_post)


@home.route('/post',methods=['POST'])
@token_required
@login_required_user
def iniciof():
    if request.method == 'POST':
        data = request.get_json()
        id = data.get("id")
        author = data.get("author")
        title = data.get("title")
        body = data.get("body")
        if not any([title,body]):
            return jsonify({"Message":"Es necesario completar todos los campos"})
        add_post(author,title,body,datetime.utcnow)
        return jsonify({"Message":"Post creado correctamente"})


@home.route('/post/<int:post_id>',methods=['PUT'])
@token_required
@login_required_user
def update_post_route(post_id):
    data = request.get_json()
    new_title = data.get('title')
    new_body = data.get('body')

    if not any([new_title,new_body]):
        return jsonify({"Message":"No hubieron cambios"})
    update_post(post_id,new_title,new_body)
    users_updated = get_post_by_id(post_id)
    print(users_updated.title)
    return jsonify({"Message":"Post actualizado"})


@home.route('/users', methods=['GET'])
@token_required
@login_required_user
def home_get_users():
    users = select_all_users()
    lista_users = [{"id": user.id, "name": user.name, "surname": user.surname, "username": user.username} for user in users]
    return jsonify(lista_users), 200


@home.route('/users/<int:id>', methods=['GET','PUT','DELETE'])
@token_required
@login_required_user
@admin_required
def home_get_user(id):
    if request.method == 'GET':
        user = get_user_by_id(id)
        if not user:
            return jsonify({"message": "Usuario no encontrado"}), 404
        return jsonify({
            "id": user.id,
            "name": user.name,
            "surname": user.surname,
            "username": user.username
        }), 200
    
    if request.method == 'PUT':
        data = request.get_json()
        new_name = data.get('name')
        new_surname = data.get('surname')
        new_username = data.get('username')
        new_password = data.get('password')
        user_to_update = get_user_by_id(id)
        if not user_to_update:
            return jsonify({"Message":"No se encontro el usuario"})
        if not any([new_name, new_surname, new_username, new_password]):
            return jsonify({"message": "No hubieron cambios"})
        update_user(id,new_name,new_surname,new_username,new_password)
        return jsonify({"message": "Usuario actualizado correctamente"})

    if request.method == 'DELETE':
        user_to_delete = get_user_by_id(id)
        if not user_to_delete: 
            return jsonify({"message": "No se encontro el usuario"})
        delete_user(user_to_delete.id)
        return jsonify({"message": "Usuario eliminado correctamente"}), 200
        

