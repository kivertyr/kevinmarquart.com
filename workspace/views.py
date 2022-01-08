from flask import Flask
from flask.blueprints import Blueprint

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return "home"
