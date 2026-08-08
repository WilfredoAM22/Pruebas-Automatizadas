import pytest
import uuid
from Backend.app import app

def correo_unico():
    return f"{uuid.uuid4().hex}@example.com"

def test_register_exitoso():
    client = app.test_client()
    response = client.post(
        "/register",
        json={"email": correo_unico(), "usuario": "user_test", "password": "MiClave123"}
    )
    assert response.status_code == 201

def test_register_sin_email():
    client = app.test_client()
    response = client.post(
        "/register",
        json={"usuario": "user_test", "password": "MiClave123"}
    )
    assert response.status_code == 400

def test_register_sin_password():
    client = app.test_client()
    response = client.post(
        "/register",
        json={"email": correo_unico(), "usuario": "user_test"}
    )
    assert response.status_code == 400

def test_register_email_invalido():
    client = app.test_client()
    response = client.post(
        "/register",
        json={"email": "correo_mal", "usuario": "user_test", "password": "MiClave123"}
    )
    assert response.status_code == 400  

def test_register_password_corta():
    client = app.test_client()
    response = client.post(
        "/register",
        json={"email": correo_unico(), "usuario": "user_test", "password": "123"}
    )
    assert response.status_code == 400  

def test_register_usuario_duplicado():
    client = app.test_client()
    email = correo_unico()
    client.post("/register", json={"email": email, "usuario": "user1", "password": "MiClave123"})
    response = client.post("/register", json={"email": email, "usuario": "user2", "password": "MiClave123"})
    assert response.status_code == 409  

def test_login_exitoso():
    client = app.test_client()
    email = correo_unico()
    client.post("/register", json={"email": email, "usuario": "user_login", "password": "MiClave123"})
    response = client.post("/login", json={"email": email, "password": "MiClave123"})
    assert response.status_code == 200

def test_login_sin_email():
    client = app.test_client()
    response = client.post("/login", json={"password": "MiClave123"})
    assert response.status_code == 400

def test_login_sin_password():
    client = app.test_client()
    response = client.post("/login", json={"email": "test@test.com"})
    assert response.status_code == 400

def test_login_email_invalido():
    client = app.test_client()
    response = client.post("/login", json={"email": "correo_mal", "password": "MiClave123"})
    assert response.status_code == 200  

def test_login_password_vacia():
    client = app.test_client()
    email = correo_unico()
    client.post("/register", json={"email": email, "usuario": "user", "password": "MiClave123"})
    response = client.post("/login", json={"email": email, "password": ""})
    assert response.status_code == 400

def test_login_respuesta_contiene_token():
    client = app.test_client()
    email = correo_unico()
    client.post("/register", json={"email": email, "usuario": "user_token", "password": "MiClave123"})
    response = client.post("/login", json={"email": email, "password": "MiClave123"})
    assert response.status_code == 200
    data = response.get_json()
    assert "token" in data