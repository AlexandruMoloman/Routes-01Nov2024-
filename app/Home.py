from flask import Blueprint

home = Blueprint("home", __name__)

@home.route("/home")
def home_page():
    return "Home Page!"