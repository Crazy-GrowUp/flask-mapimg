from flask import Blueprint, render_template

hello = Blueprint('hello', __name__, url_prefix='/')

@hello.route('/')
def index():
    return render_template("index.html")