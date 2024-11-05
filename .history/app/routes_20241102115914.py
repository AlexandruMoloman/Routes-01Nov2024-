from flask import Blueprint

main = Blueprint("main", __name__)

post =Blueprint("main", __name__)

@main.route("/")
def home():
    return "Welcome to the Main Page"

@post.route("/")
def posts():
    return "Posts Page"