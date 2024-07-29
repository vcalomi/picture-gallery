from models.Picture import Picture
from models.User import User
from config import db
from service.picture_service import _serialize_picture, delete_user_pictures

def create_user(user_data):
    if not user_data or not "username" in user_data or not "email" in user_data or not "password" in user_data:
        raise Exception("Missing data")
    
    name = user_data["username"]
    email = user_data["email"]
    password = user_data["password"]

    new_user = User(username=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return _serialize_user(new_user)

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        raise Exception("User doesn't exist")
    
    delete_user_pictures(user_id)
    
    db.session.delete(user)
    db.session.commit()

def get_all_users():
    users = User.query.all()
    if not users:
        raise Exception("There are not any users yet")
    
    json_users = [_serialize_user(user) for user in users]
    return json_users

def check_credentials(data):
    if not "username" in data or not "password" in data:
        raise Exception("Missing fields")
    
    username = data["username"]
    password = data["password"]
    
    user = User.query.filter_by(username=username).first()

    if user.password != password:
        raise Exception("Incorrect password")
    
    return _serialize_user(user)

def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        raise Exception("User not found")
    return _serialize_user(user)

def _serialize_user(user):
    pictures = [_serialize_picture(picture) for picture in user.pictures]
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "pictures": pictures
    }