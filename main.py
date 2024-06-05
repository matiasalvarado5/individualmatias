from src import app
from src.database.create_db import create_db_and_table


if __name__ == '__main__':
    create_db_and_table()
    app.run()