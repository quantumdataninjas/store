import os
from flask import Flask

# from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt
from flask_argon2 import Argon2


db = SQLAlchemy()
toolbar = DebugToolbarExtension()
cors = CORS()
mail = Mail()
migrate = Migrate()
# bcrypt = Bcrypt()
argon2 = Argon2()

def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    app.config.update(
        # DEBUG=False,
        # DEBUG=True,
        # MAIL_DEBUG=False,
        #EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        #MAIL_PORT=587,
        #MAIL_USE_TLS=1,
        MAIL_USERNAME = 'hardheadhacker@gmail.com',
        MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")#environ['MAIL_PASSWORD']
    )

    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    # bcrypt.init_app(app)
    argon2.init_app(app)

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
