from flask import Blueprint

post = Blueprint('post', __name__)

@post.route('/post')
def show_post():
    return "Welcome to the Post Page!"
