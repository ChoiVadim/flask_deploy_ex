from flask import render_template, request, url_for, redirect, Blueprint

test_routes = Blueprint('test', __name__, template_folder="templates")

@test_routes.route('/')
def home():
    msg = "Hello, vadim"
    return render_template("main/index.html", message=msg)

@test_routes.route('/login')
def login():
    username = request.form.get("username")
    return render_template("login.html")

@test_routes.route('/test')
def test():
    return redirect(url_for('new'))

@test_routes.route('/new')
def new():
    return render_template('new.html', name='vadim')
