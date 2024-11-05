from flask import Blueprint

post = Blueprint("posts", __name__)

from flask import Flask
@posts.route("/")
def posts():
    return "Posts Page"