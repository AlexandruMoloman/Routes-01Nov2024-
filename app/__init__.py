from flask import Flask
from .routes import main
from .post import post  
from .Home import home
from .contacts import contacts
from .service import service

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(post)  
    app.register_blueprint(home)
    app.register_blueprint(contacts)
    app.register_blueprint(service)
    return app
