import mysql.connector
from .connection import get_db_connection, get_server_connection

def create_db():
    try:
        server = get_server_connection()
        if server is None:
            print("Usuario y/o contraseña no correctos")
        else:
            cursor = server.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS utn_project_db")
            cursor.close()
            server.close()
            print("Base de datos creada o ya existente")
    except mysql.connector.Error as err:
        print(f"Error al crear la base de datos:{err}")

def create_table():
    try:
        db = get_db_connection()
        if db is None:
            print("No se pudo establecer conexión con la base de datos.")
        else:
            cursor = db.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(25),
                    surname VARCHAR(25),
                    username VARCHAR(25),
                    password TINYTEXT)
                            """)
            db.commit()
            cursor.close()
            db.close()
            print("Tabla creada o ya existente.")
    except mysql.connector.Error as err:
        print(f"Error al crear la tabla: {err}")

def create_db_and_table():
    create_db()
    create_table()
