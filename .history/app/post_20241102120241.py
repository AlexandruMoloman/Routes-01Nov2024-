import flask from Blueprint

post = Blueprint("main", __name__)

from flask import Flask
@post.route("/")
def posts():
    return "Posts Page"