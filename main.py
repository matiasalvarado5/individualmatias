from app.database.create_db import create_db_and_table
from app import create_app

def main():
    create_db_and_table()
    app = create_app()
    app.run()

if __name__ == '__main__':
    main()
