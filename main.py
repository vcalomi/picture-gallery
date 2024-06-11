from flask import Flask, jsonify, request
from config import db
from models.User import User

app = Flask(__name__)
port: int = 5000

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:0402@localhost/photo_gallery"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def main():
    return "<h1>Hello world</h1>"

@app.route("/create/user", methods=['POST'])
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

if __name__ == "__main__":
    print("Starting server...")
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True, port=port)