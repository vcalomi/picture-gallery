from flask import jsonify, request
from models.User import User
from config import db

def create_user():
    data = request.get_json()

    if not data or not "username" in data or not "email" in data:
        return jsonify({"message": "Missing fields"}), 400
    
    name = data["username"]
    email = data["email"]
    password = data["password"]

    new_user = User(username=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created succesfully"}), 201

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User doesn't exist"}), 404
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"}), 200