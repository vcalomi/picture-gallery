from flask import jsonify, request, Blueprint
from models.User import User
from config import db
from service.user_service import _serialize_user, check_credentials, create_user, delete_user, get_all_users, get_user_by_username

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    new_user = None
    try:
        new_user = create_user(data)
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify(new_user), 201

@user_bp.route("/delete/<user_id>", methods=["DELETE"])
def erase_user(user_id):
    try:
        delete_user(user_id)
    except Exception as e:
        return jsonify({"message": str(e)}), 404
    return jsonify({"message": "User deleted"}), 200

@user_bp.route("/", methods=["GET"])
def get_users():
    try:
        json_users = get_all_users()
    except Exception as e:
        return jsonify({"message": str(e)}), 404

    return jsonify(json_users, 200)

@user_bp.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()
    try:
        user = check_credentials(data)
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify(user), 200

@user_bp.route("/<username>", methods=["GET"])
def get_user(username):

    try:
        user = get_user_by_username(username)
    except Exception as e:
        return jsonify({"message": str(e)}), 404

    return jsonify(user), 200