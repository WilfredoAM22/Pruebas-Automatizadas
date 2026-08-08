import bcrypt
import jwt
import re
from datetime import datetime, timedelta, UTC


SECRET_KEY = "MiClaveSecretaParaJWT2026_MiRed_Segura"


def validate_email(email):
    """
    Valida que el email tenga un formato básico correcto.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email) is not None


def validate_password(password):
    """
    Valida que la contraseña tenga al menos 8 caracteres,
    una letra y un número.
    """
    if len(password) < 8:
        return False

    if not re.search(r"[A-Za-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    return True


def hash_password(password):
    password_bytes = password.encode("utf-8")
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    return hashed.decode("utf-8")


def verify_password(password, hashed_password):
    password_bytes = password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")

    return bcrypt.checkpw(password_bytes, hashed_bytes)


def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.now(UTC) + timedelta(hours=1)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return token


def verify_token(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None
