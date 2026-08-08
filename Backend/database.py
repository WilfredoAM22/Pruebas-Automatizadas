import sqlite3
from Backend.auth import hash_password

DATABASE = "Backend/mired.db"


def crear_base_datos():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    usuarios = [
        ("alexis@example.com", hash_password("MiClave123")),
        ("maria@example.com", hash_password("Maria123")),
        ("juan@example.com", hash_password("Juan123"))
    ]

    for email, password in usuarios:
        try:
            cursor.execute(
                "INSERT INTO usuarios (email, password) VALUES (?, ?)",
                (email, password)
            )
        except sqlite3.IntegrityError:
            pass

    conexion.commit()
    conexion.close()


if __name__ == "__main__":
    crear_base_datos()

