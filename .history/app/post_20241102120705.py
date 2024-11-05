from flask import Blueprint

posts = Blueprint("posts", __name__)

from flask import Flask
@posts.route("/")
def show_posts():
    return "Posts Page"