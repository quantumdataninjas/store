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


class GetSimpleUsers(Resource):
    def get(self):
        """Get all simple users"""
        return {
            "data": {
                "simple_users": [
                    simple_user.to_dict()
                    for simple_user in SimpleUser.query.all()
                ]
            }
        }, 200


class GetSimpleUser(Resource):
    def get(self, simple_user_id):
        """Get single simple_user details"""
        try:
            simple_user = SimpleUser.query.filter_by(
                id=int(simple_user_id)
            ).first()
            if not simple_user:
                return {"message": "User does not exist."}, 404
            else:
                return {"data": simple_user.to_dict()}, 200
        except ValueError as ve:
            return {"message": f"Value Error: {ve}"}, 404


class GetUsers(Resource):
    def get(self):
        """Get all users"""
        return {
            "data": {"users": [user.to_dict() for user in User.query.all()]}
        }, 200


class GetUser(Resource):
    def get(self, user_id):
        """Get single user details"""
        try:
            user = User.query.filter_by(id=int(user_id)).first()
            if not user:
                return {"message": "User does not exist."}, 404
            else:
                return {"data": user.to_dict()}, 200
        except ValueError as ve:
            return {"message": f"Value Error: {ve}."}, 404


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
api.add_resource(GetSimpleUsers, "/users/simple")
api.add_resource(GetSimpleUser, "/users/simple/<simple_user_id>")
api.add_resource(GetUsers, "/users")
api.add_resource(GetUser, "/users", "/users/<user_id>")
api.add_resource(Subscribe, "/users/subscribe")
api.add_resource(Register, "/users/register")
