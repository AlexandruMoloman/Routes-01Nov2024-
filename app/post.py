from flask import Blueprint

post = Blueprint('post', __name__)

@post.route('/posts') 
def show_post():
    return "Welcome to the Post Page!"
