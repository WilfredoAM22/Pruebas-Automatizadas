from flask import Flask, request, jsonify
from flask_cors import CORS
from Backend.auth import hash_password, verify_password, generate_token
import sqlite3


app = Flask(__name__)

CORS(app)

DATABASE = "Backend/mired.db"


def conectar():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion


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


    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE email = ?",
        (email,)
    )

    usuario_existente = cursor.fetchone()


    if usuario_existente:
        conexion.close()

        return jsonify({
            "error": "El usuario ya existe"
        }), 409


    password_hash = hash_password(password)


    cursor.execute(
        """
        INSERT INTO usuarios(email, password)
        VALUES (?, ?)
        """,
        (email, password_hash)
    )


    conexion.commit()
    conexion.close()


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



    conexion = conectar()
    cursor = conexion.cursor()


    cursor.execute(
        "SELECT * FROM usuarios WHERE email = ?",
        (email,)
    )


    usuario = cursor.fetchone()

    conexion.close()


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





















