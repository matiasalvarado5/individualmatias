from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session
from src.database import db, cursor
from src.routes.auth import login_required

home = Blueprint('home', __name__,url_prefix='/home')

@home.route("/")
@login_required
def homef():
    return render_template('home/home.html')

