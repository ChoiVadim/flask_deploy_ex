from flask import render_template, request, url_for, redirect, Blueprint

test_routes = Blueprint('test', __name__, template_folder="templates")

@test_routes.route('/')
def home():
    return render_template("index.html")

@test_routes.route('/login')
def login():
    return render_template("login.html")

@test_routes.route('/switch')
def switch():
    return render_template("switch.html")

@test_routes.route("/upload")
def upload():
    return render_template("upload.html")