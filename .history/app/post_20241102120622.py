from flask import Blueprint

posts = Blueprint("posts", __name__)

from flask import Flask
@posts.route("/")
def posts():
    return "Posts Page"