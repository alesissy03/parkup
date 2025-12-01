# TODO:
# inițializează aplicația Flask
# încarcă configurația (din config.py)
# inițializează extensiile (SQLAlchemy, LoginManager)
# înregistrează Blueprints (auth, parking, reservations, admin)

from flask import Flask
from app.routes import register_blueprints

def create_app():
    app = Flask(__name__)
    # ...
    register_blueprints(app)
    return app
