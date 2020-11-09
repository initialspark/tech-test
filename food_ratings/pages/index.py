from food_ratings.pages.blueprint import main
from flask import render_template


@main.route("/", methods=["GET"])
def get_default():
    return render_template("index.html")
