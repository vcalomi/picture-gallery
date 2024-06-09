from flask import Flask


app = Flask(__name__)
port: int = 5000


@app.route("/")
def main():
    return "<h1>Hello world</h1>"






if __name__ == "__main__":
    print("Starting server...")
    app.run(host="0.0.0.0", debug=True, port=port)