from Backend.auth import (
    hash_password,
    verify_password,
    generate_token,
    verify_token
)


def test_hash_password():
    password = "MiClave123"

    hashed = hash_password(password)

    assert hashed != password
    assert isinstance(hashed, str)


def test_verify_password_correcta():
    password = "MiClave123"

    hashed = hash_password(password)

    assert verify_password(password, hashed) is True


def test_verify_password_incorrecta():
    password = "MiClave123"

    hashed = hash_password(password)

    assert verify_password("ClaveIncorrecta", hashed) is False


def test_generate_token():
    token = generate_token(1)

    assert token is not None
    assert isinstance(token, str)


def test_verify_token():
    token = generate_token(1)

    payload = verify_token(token)

    assert payload is not None
    assert payload["user_id"] == 1


def test_token_invalido():
    payload = verify_token("token-invalido")

    assert payload is None