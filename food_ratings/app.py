from flask import Flask
from food_ratings.pages import blueprint


def create_app():
    app = Flask(__name__, static_url_path="/assets")
    app.register_blueprint(blueprint.main)
    return app
