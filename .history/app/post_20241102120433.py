from flask import Blueprint

post = Blueprint("post", __name__)

from flask import Flask
@post.route("/")
def posts():
    return "Posts Page"