from flask import jsonify, request, Blueprint
from models.Photo import Photo
from models.User import User
from config import db
from service.photo_service import create_photo, delete_photo

photo_bp = Blueprint("photo_bp", __name__)

@photo_bp.route("/upload/<username>", methods=["POST"])
def upload_photo(username):
    data = request.get_json()
    try:
        create_photo(username, data)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message":"New photo added"}), 201

@photo_bp.route("/delete/<photo_id>", methods=["DELETE"])
def erase_photo(user_id, photo_id):

    try:
        delete_photo(user_id, photo_id)
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify({"message":"Photo deleted"}), 200