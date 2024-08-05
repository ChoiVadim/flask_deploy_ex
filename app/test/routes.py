from flask import render_template, request, url_for, redirect, Blueprint, session
from werkzeug.security import check_password_hash, generate_password_hash

from app.test.models import User
from app.app import db


test_routes = Blueprint("test", __name__, template_folder="templates")


@test_routes.route("/")
def home():
    return render_template("index.html")


@test_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.user_id
            return redirect("/upload")
        else:
            return render_template(
                "login.html", message="Invalid username or password."
            )

    return render_template("login.html")


@test_routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        if not (username and password and email):
            return render_template("register.html", message="All fields are required.")

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


@test_routes.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@test_routes.route("/switch")
def switch():
    return render_template("switch.html")


@test_routes.route("/upload", methods=["GET"])
def upload():
    return render_template("upload.html")
