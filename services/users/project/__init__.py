import os
from flask import Flask

# from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS


# db = SQLAlchemy()
# toolbar = DebugToolbarExtension()
# cors = CORS()


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    db = SQLAlchemy(app)
    toolbar = DebugToolbarExtension(app)
    # toolbar.init_app(app)
    cors = CORS(app)
    # cors.init_app(app)

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
