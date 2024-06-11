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

if __name__ == "__main__":
    print("Starting server...")
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True, port=port)