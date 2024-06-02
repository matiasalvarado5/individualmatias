import mysql.connector
from .db_config import MYSQL_CONFIG

try:
    db = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = db.cursor() 
    print(f"Conexion exitosa con la base de datos")

except mysql.connector.Error as Err:
    print("Error en la conbexion con la base de datos")

