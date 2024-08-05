import os
from flask import render_template, request, url_for, redirect, Blueprint, session, send_from_directory
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from app.test.models import User
from app.app import db
from app.config import Config


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


def allowed_file(filename):
    allowed_extensions = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

@test_routes.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            return render_template("upload.html", message='No file part')
        
        file = request.files['file']
        
        if file.filename == '':
            return render_template("upload.html", message='No selected file')
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            return render_template("upload.html", message='File successfully uploaded')
        else:
            return render_template("upload.html", message='Invalid file type')
    
    return render_template("upload.html")

@test_routes.route("/files")
def list_files():
    files = os.listdir(Config.UPLOAD_FOLDER)
    return render_template("files.html", files=files)

@test_routes.route('/download/<path:filename>', methods=['GET', 'POST'])
def download_file(filename):
    uploads = os.path.join("/home/vadim/Desktop/flask_app/", Config.UPLOAD_FOLDER)
    return send_from_directory(uploads, filename)
