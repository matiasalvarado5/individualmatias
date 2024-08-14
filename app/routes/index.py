from flask import render_template, Blueprint, flash, g, redirect, request, url_for, session


index = Blueprint('index', __name__)

@index.route("/",methods=['GET'])
def indexf():
    return render_template('index/index.html')

