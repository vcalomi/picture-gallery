from flask import jsonify, request
from models.Photo import Photo
from models.User import User
from config import db

def upload_photo(user_id):
    
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message":"A user that doesn't exist can't upload a photo"}), 400

    data = request.get_json()
    if not data or not "name" in data or not "url" in data:
        return jsonify({"message": "Missing fields"}), 400
    
    name = data["name"]
    url = data["url"]
    description = data.get("description", "")

    new_photo = Photo(name, description, url, user_id)
    db.session.add(new_photo)
    db.session.commit()

    return jsonify({"message":"New photo added"}), 201
