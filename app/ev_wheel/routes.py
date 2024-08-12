from flask import Blueprint, render_template

ev_wheels_routes = Blueprint("ev_wheel", __name__, template_folder="templates", static_folder="app/ev_wheel/")

@ev_wheels_routes.route("/wheel")
def wheel():
    return render_template("wheel.html")