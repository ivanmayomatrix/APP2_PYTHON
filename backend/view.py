from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from controller import Controller

app = Flask(__name__, static_folder='../frontend')
CORS(app)
controller = Controller()

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if controller.register_user(data["username"], data["password"]):
        return jsonify({"message": "User registered successfully!"}), 201
    return jsonify({"message": "Username already exists."}), 400

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]
    print(f"Intentando iniciar sesión con usuario: {username} y contraseña: {password}")
    if controller.login_user(username, password):
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials."}), 401

@app.route("/products", methods=["GET"])
def products():
    products = controller.fetch_products()
    return jsonify(products), 200

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

@app.route('/')
def root():
    return send_from_directory(app.static_folder, 'login.html')


if __name__ == "__main__":
    app.run(debug=True)
