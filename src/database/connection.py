import mysql.connector
from src.database.db_config import MYSQL_CONFIG


def get_server_connection():
    config = MYSQL_CONFIG.copy()
    config.pop('database')

    try:
        server = mysql.connector.connect(**config)
        print("Conexion con el servidor exitosa")
        return server
        
    except mysql.connector.Error as Err:
        print("Error en la conexion con el servidor")


def get_db_connection():
    try:
        db = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = db.cursor() 
        print("Conexion exitosa con la base de datos")
        return db

    except mysql.connector.Error as Err:
        print("La base de datos no existe")


