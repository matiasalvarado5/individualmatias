from flask import Flask, redirect,url_for

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Import views}
from src.routes.index import index
from src.routes.auth import auth
from src.routes.home import home

app.register_blueprint(index)
app.register_blueprint(auth)
app.register_blueprint(home)
