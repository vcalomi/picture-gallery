from flask import jsonify, request, Blueprint
from models.Photo import Photo
from models.User import User
from config import db

photo_bp = Blueprint("photo_bp", __name__)

@photo_bp.route("/create/<user_id>", methods=["POST"])
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

@photo_bp.route("/delete/<photo_id>", methods=["DELETE"])
def delete_photo(user_id, photo_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({"message":"A user that doesn't exist can't delete a photo"}), 400

    photo = Photo.query.get(photo_id)

    if not photo:
        return jsonify({"message":"The photo doesn't exist"}), 400
    
    db.session.delete(photo)
    db.session.commit()

    return jsonify({"message":"Photo deleted"}), 200