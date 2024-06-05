from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session
from src.services.UserServices import login_required_user,logged_user

home = Blueprint('home', __name__,url_prefix='/home')

@login_required_user
@home.route("/")
def homef():
    return render_template('home/home.html')

@login_required_user
@home.route("/civil")
def civilf():
    return render_template('home/home.html')