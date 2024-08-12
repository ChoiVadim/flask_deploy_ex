from flask import Blueprint, render_template

ev_wheels_routes = Blueprint("ev_wheel", __name__, template_folder="templates")

@ev_wheels_routes.route("/wheel")
def wheel():
    return render_template("wheel.html")

@ev_wheels_routes.route("/ev_wheel")
def ev_wheel():
    return render_template("ev_wheel.html")