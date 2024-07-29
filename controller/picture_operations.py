from flask import jsonify, request, Blueprint
from models.Picture import Picture
from models.User import User
from config import db
from service.picture_service import create_picture, delete_picture

picture_bp = Blueprint("picture_bp", __name__)

@picture_bp.route("/upload/<username>", methods=["POST"])
def upload_picture(username):
    data = request.get_json()
    try:
        picture = create_picture(username, data)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify(picture), 201

@picture_bp.route("/delete/<username>/<picture_id>", methods=["DELETE"])
def erase_picture(username, picture_id):
    try:
        delete_picture(username, picture_id)
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify({"message":"Picture deleted"}), 200