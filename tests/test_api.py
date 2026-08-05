from Backend.app import app
import uuid


def correo_unico():
    return f"{uuid.uuid4().hex}@example.com"


def test_register():
    client = app.test_client()

    response = client.post(
        "/register",
        json={
            "email": correo_unico(),
            "usuario": "usuario_test",
            "password": "MiClave123"
        }
    )

    assert response.status_code == 201


def test_login_correcto():
    client = app.test_client()

    email = correo_unico()

    client.post(
        "/register",
        json={
            "email": email,
            "usuario": "login_test",
            "password": "MiClave123"
        }
    )

    response = client.post(
        "/login",
        json={
            "email": email,
            "password": "MiClave123"
        }
    )

    assert response.status_code == 200

    datos = response.get_json()

    assert "token" in datos


def test_login_password_incorrecta():
    client = app.test_client()

    email = correo_unico()

    client.post(
        "/register",
        json={
            "email": email,
            "usuario": "error_test",
            "password": "MiClave123"
        }
    )

    response = client.post(
        "/login",
        json={
            "email": email,
            "password": "Incorrecta"
        }
    )

    assert response.status_code == 401


def test_login_usuario_inexistente():
    client = app.test_client()

    response = client.post(
        "/login",
        json={
            "email": "noexiste@example.com",
            "password": "MiClave123"
        }
    )

    assert response.status_code == 401