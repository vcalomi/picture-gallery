from flask import Flask
from config import db
from controller.user_operations import user_bp
from controller.photo_operations import photo_bp
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)
port: int = 5000

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def main():
    return "<h1>Hello world</h1>"

app.register_blueprint(user_bp, url_prefix="/api/user")

app.register_blueprint(photo_bp, url_prefix="/api/photo")

if __name__ == "__main__":
    print("Starting server...")
    app.run(host="0.0.0.0", debug=True, port=port)