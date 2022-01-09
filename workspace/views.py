from flask import Flask
from flask import Blueprint, render_template


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/hvaderkatte")
def hvaderkatte():
    return render_template("hvaderkatte.html")

@views.route("/kevinmarquart")
def kevinmarquart():
    return render_template("kevinmarquart.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/projects")
def projects():
    return render_template("projects.html")