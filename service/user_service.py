from models.User import User
from config import db

def create_user(user_data):
    if not user_data or not "username" in user_data or not "email" in user_data or not "password" in user_data:
        raise Exception("Missing data")
    
    name = user_data["username"]
    email = user_data["email"]
    password = user_data["password"]

    new_user = User(username=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return new_user