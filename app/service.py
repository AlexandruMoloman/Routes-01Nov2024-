from flask import Blueprint

service = Blueprint("service", __name__)

@service.route("/service")
def show_service():
    return "Congratulations I am Service!"