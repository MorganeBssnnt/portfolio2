from flask import Blueprint, render_template

# Création d'un blueprint pour organiser les routes
main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")
