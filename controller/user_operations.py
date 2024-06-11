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

def serialize_photo(photo):
    return {
        "id": photo.id,
        "name": photo.name,
        "description": photo.description,
        "url": photo.url,
        "created_at": photo.created_at.strftime("%Y-%m-%d %H:%M")
    }

def serialize_user(user):
    photos = [serialize_photo(photo) for photo in user.photos]
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "photos": photos
    }

def get_users():
    users = User.query.all()
    if not users:
        return jsonify({"message": "There isn't any users"}), 404
    
    json_users = [serialize_user(user) for user in users]

    return jsonify(json_users, 200)