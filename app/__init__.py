from flask import Flask
from .routes import main


def create_app():
    app= Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.register_blueprint(main)

    return app