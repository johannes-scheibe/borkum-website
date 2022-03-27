from flask import Blueprint, render_template, current_app as app


home = Blueprint('home', __name__)

@home.route('/')
def init():
    return render_template("index.html",  contact=app.config['CONTACT'])

