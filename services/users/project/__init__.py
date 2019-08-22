import os
from flask import Flask

# from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS


new_simple_user_dict = {"email": "user@test.org"}
new_simple_user_dict2 = {"email": "user2@test.org"}
new_user_dict = {
    "email": "user@test.org",
    "subscribed": True,
    "terms_and_conditions": True,
    "firstname": "first",
    "middlename": "middle",
    "lastname": "last",
    "address1": "1523 John St",
    "address2": None,
    "city": "Fort Lee",
    "state": "NJ",
    "zipcode": "07024",
    "country": "United States",
    "phone": None,
    "birthmonth": "January",
    "birthday": "01",
    "birthyear": "1990",
}
new_user_dict2 = {
    "email": "user2@test.org",
    "subscribed": True,
    "terms_and_conditions": True,
    "firstname": "first",
    "middlename": "middle",
    "lastname": "last",
    "address1": "1523 John St",
    "address2": None,
    "city": "Fort Lee",
    "state": "NJ",
    "zipcode": "07024",
    "country": "United States",
    "phone": None,
    "birthmonth": "January",
    "birthday": "01",
    "birthyear": "1990",
}

db = SQLAlchemy()
toolbar = DebugToolbarExtension()
cors = CORS()


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app)

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
