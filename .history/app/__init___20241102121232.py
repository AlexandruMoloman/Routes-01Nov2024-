from flask import Flask
from .routes import main
from .post import post  
from .Home import home

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(post)  
    app.register_blueprint(home)
    return app
