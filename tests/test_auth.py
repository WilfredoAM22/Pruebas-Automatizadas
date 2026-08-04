from Backend.auth import (
    validate_email,
    validate_password,
    hash_password,
    verify_password,
    generate_token,
    verify_token
)


def test_validate_email_correcto():
    assert validate_email("usuario@gmail.com") is True


def test_validate_email_incorrecto():
    assert validate_email("usuario@") is False


def test_validate_password_correcta():
    assert validate_password("MiClave123") is True


def test_validate_password_muy_corta():
    assert validate_password("Clave1") is False


def test_validate_password_sin_numero():
    assert validate_password("MiClaveSegura") is False


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
