from flask import Flask
from flask import Blueprint, render_template


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/hvaderkatte")
def hvaderkatte():
    return render_template("hvaderkatte.html")