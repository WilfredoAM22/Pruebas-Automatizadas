from Backend.app import app


def test_register():
    client = app.test_client()

    response = client.post(
        "/register",
        json={
            "email": "test@example.com",
            "password": "MiClave123"
        }
    )

    assert response.status_code == 201


def test_login_correcto():
    client = app.test_client()

    client.post(
        "/register",
        json={
            "email": "login@example.com",
            "password": "MiClave123"
        }
    )

    response = client.post(
        "/login",
        json={
            "email": "login@example.com",
            "password": "MiClave123"
        }
    )

    assert response.status_code == 200

    datos = response.get_json()

    assert "token" in datos


def test_login_password_incorrecta():
    client = app.test_client()

    client.post(
        "/register",
        json={
            "email": "error@example.com",
            "password": "MiClave123"
        }
    )

    response = client.post(
        "/login",
        json={
            "email": "error@example.com",
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
