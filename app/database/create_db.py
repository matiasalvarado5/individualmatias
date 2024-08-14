from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from app.database.connection import get_server_connection, get_db_connection, Base
from app.models.users import User
from app.models.post import Post

def create_db():
    try:
        server_engine = get_server_connection()
        if not server_engine:
            print("Usuario y/o contraseña no correctos")
        
        with server_engine.connect() as connection:
            db_exists = connection.execute(text("SELECT 1 FROM pg_database WHERE datname='utn_project_db'")).scalar()
            if db_exists:
                print("Base de datos ya existente")
            else:
                connection.execute(text("commit"))
                connection.execute(text("CREATE DATABASE utn_project_db"))
                print("Base de datos creada con exito")
            server_engine.dispose()
    except SQLAlchemyError as err:
        print(f"Error al crear la base de datos: {err}")

def create_table():
    try:
        session, engine = get_db_connection()
        if not session or not engine:
            print("No se pudo establecer conexión con la base de datos.")
        else:
            Base.metadata.create_all(engine)
            engine.dispose()
    except SQLAlchemyError as err:
        print(f"Error al crear la tabla: {err}")

def create_db_and_table():
    create_db()
    create_table()
