from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc
from project import db
from project.api.models import SimpleUser, User


users_blueprint = Blueprint("users", __name__)
api = Api(users_blueprint)


class Ping(Resource):
    def get(self):
        return {"message": "pong!"}, 200


class Subscribe(Resource):
    def post(self):
        post_data = request.get_json()
        if not post_data:
            return {"message": "Invalid payload."}, 400
        email = post_data.get("email")
        try:
            simple_user = SimpleUser.query.filter_by(email=email).first()
            if not simple_user:
                db.session.add(SimpleUser(email=email, subscribed=True))
                db.session.commit()
                return {"message": f"{email} is subscribed!"}, 201
            else:
                return {"message": f"User {email} is already subscribed."}, 400
        except exc.IntegrityError as ie:
            db.session.rollback()
            return {"message": f"Integrity Error: {ie}"}, 400


class Register(Resource):
    def post(self):
        post_data = request.get_json()
        if not post_data:
            return {"message": "Invalid payload."}, 400
        email = post_data.get("email")
        try:
            user = User.query.filter_by(email=email).first()
            if not user:
                db.session.add(User(**post_data))
                simple_user = SimpleUser.query.filter_by(email=email).first()
                if simple_user:
                    simple_user.registered = True
                else:
                    db.session.add(
                        SimpleUser(
                            email=email,
                            subscribed=post_data.get("subscribed"),
                            registered=True,
                        )
                    )
                db.session.commit()
                return {"message": f"{email} is registered!"}, 201
            else:
                return {"message": f"User {email} already exists."}, 400
        except exc.IntegrityError as ie:
            db.session.rollback()
            return {"message": f"Integrity Error: {ie}"}, 400


api.add_resource(Ping, "/users/ping")
api.add_resource(Subscribe, "/users/subscribe")
api.add_resource(Register, "/users/register")
