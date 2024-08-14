from app.database.create_db import create_db_and_table
from app import create_app


if __name__ == '__main__':
    create_db_and_table()
    create_app().run()