import os

MYSQL_CONFIG = {
    'host': os.environ.get("database_host"),
    'user': os.environ.get("database_user"),
    'password': os.environ.get("database_password"),
    'database': os.environ.get("database"),
}