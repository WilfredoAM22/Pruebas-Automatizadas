from flask import Flask, request, jsonify
from Backend.auth import hash_password, verify_password, generate_token

app = Flask(__name__)

# Base de datos temporal en memoria
usuarios = {}


@app.route("/")
def inicio():
    return "Backend de MiRed funcionando correctamente"


@app.route("/register", methods=["POST"])
def register():
    datos = request.get_json()

    email = datos.get("email")
    password = datos.get("password")

    if not email or not password:
        return jsonify({
            "error": "Email y contraseña son obligatorios"
        }), 400

    if email in usuarios:
        return jsonify({
            "error": "El usuario ya existe"
        }), 409

    usuarios[email] = {
        "password": hash_password(password)
    }

    return jsonify({
        "mensaje": "Usuario registrado correctamente"
    }), 201


@app.route("/login", methods=["POST"])
def login():
    datos = request.get_json()

    email = datos.get("email")
    password = datos.get("password")

    if not email or not password:
        return jsonify({
            "error": "Email y contraseña son obligatorios"
        }), 400

    usuario = usuarios.get(email)

    if not usuario:
        return jsonify({
            "error": "Credenciales incorrectas"
        }), 401

    if not verify_password(password, usuario["password"]):
        return jsonify({
            "error": "Credenciales incorrectas"
        }), 401

    token = generate_token(email)

    return jsonify({
        "mensaje": "Login exitoso",
        "token": token
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
