from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def get_server_connection():
    try:
        # Conectar al servidor de PostgreSQL
        engine = create_engine(f'postgresql+psycopg2://{os.environ.get("database_user")}:{os.environ.get("database_password")}@localhost/')
        return engine
    except Exception as e:
        print(f"Error al conectar al servidor: {e}")
        return None

def get_db_connection():
    try:
        # Conectar a la base de datos específica
        engine = create_engine(f'postgresql+psycopg2://{os.environ.get("database_user")}:{os.environ.get("database_password")}@localhost/utn_project_db')
        Session = sessionmaker(bind=engine)
        session = Session()
        return session, engine
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None