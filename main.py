from flask import Flask, jsonify, request
from config import db
from controller.user_operations import *
from controller.photo_operations import *

app = Flask(__name__)
port: int = 5000

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:0402@localhost/photo_gallery"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def main():
    return "<h1>Hello world</h1>"

@app.route("/create/user", methods=['POST'])
def create_user_route():
    return create_user()

@app.route("/delete/user/<user_id>", methods=['DELETE'])
def delete_user_route(user_id):
    return delete_user(user_id)

@app.route("/add/photo/<user_id>", methods=["POST"])
def upload_photo_route(user_id):
    return upload_photo(user_id)

@app.route("/delete/photo/<user_id>/<photo_id>", methods=["DELETE"])
def delete_photo_route(user_id, photo_id):
    return delete_photo(user_id, photo_id)

if __name__ == "__main__":
    print("Starting server...")
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True, port=port)