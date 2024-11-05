from flask import Blueprint

contacts =Blueprint("contacts", __name__)

@contacts.route("/contacts")
def show_cont():
    return "I am Contacts!"