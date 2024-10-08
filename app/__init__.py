from flask import Flask, redirect,url_for
from app.database.create_db import create_db_and_table
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')


    create_db_and_table()

    # Import views
    from app.routes.index import index
    from app.routes.auth import auth
    from app.routes.home import home

    app.register_blueprint(index)
    app.register_blueprint(auth)
    app.register_blueprint(home)
 
    return app
