from flask import Flask
from .routes import main
from .post import post  
from .Home import home
from .contacts import contacts

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(post)  
    app.register_blueprint(home)
    app.register_blueprint(contacts)
    return app
