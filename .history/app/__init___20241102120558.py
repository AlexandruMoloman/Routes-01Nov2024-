from flask import Flask
from .routes import main
from .post import posts

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(posts)
    return app