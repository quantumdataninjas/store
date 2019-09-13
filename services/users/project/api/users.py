from datetime import datetime
from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc
from project import db
from project.api.models import (
    SimpleUser,
    User,
    Address,
    UserAddress,
)
from project.utils import validate_email, send_test_email


users_blueprint = Blueprint("users", __name__)
api = Api(users_blueprint)


class Ping(Resource):
    """
    Ping Pong
    """

    def get(self):
        # addresses = UserAddress.query.all()
        return {
            "message": "pong!",
            # "data": [address.to_dict() for address in addresses]
        }, 200


class SimpleUsers(Resource):
    """
    SimpleUser Api
    """

    def get(self):
        """
        Get all simple users.
        """
        return {
            "simple_users": [
                simple_user.to_dict()
                for simple_user in SimpleUser.query.all()
            ]
        }, 200


class GetSimpleUser(Resource):
    def get(self, simple_user_id):
        """
        Get single simple_user details.
        """
        try:
            simple_user = SimpleUser.query.filter_by(
                id=int(simple_user_id)
            ).first()
            if not simple_user:
                return {
                    "message": "User does not exist."
                }, 404
            return {
                "simple_user": simple_user.to_dict()
            }, 200
        except ValueError as ve:
            return {
                "message": f"Value Error: {ve}"
            }, 404


class Subscribe(Resource):
    def post(self):
        post_data = request.get_json()
        if not post_data:
            return {
                "message": "Invalid payload."
            }, 400
        try:
            email = post_data["email"]
            if not validate_email(email):
                return {
                    "message": f"{email} is not a valid email."
                }, 400
            if SimpleUser.query.filter_by(email=email).first():
                return {
                    "message": f"Email {email} is already subscribed."
                }, 400
            db.session.add(SimpleUser(**post_data))
            db.session.commit()
            # send email
            mail_message = send_test_email()
            return {
                "message": f"{email} is subscribed!",
                "message2": mail_message
            }, 201
        except TypeError:
            return {
                "message": f"Type Error: Post data must be JSON."
            }, 400
        except KeyError as ke:
            return {
                "message": f"Key Error: {ke}"
            }, 400
        except exc.IntegrityError as ie:
            db.session.rollback()
            return {
                "message": f"Integrity Error: {ie}"
            }, 400

        # finally:
        #     return {"message": message}, status_code


class Unsubscribe(Resource):
    def get(self, simple_user_id):
        """
        Get single simple_user details.
        """
        try:
            simple_user = SimpleUser.query.filter_by(
                id=int(simple_user_id)
            ).first()
            if not simple_user:
                return {
                    "message": "User does not exist.",
                }, 404
            simple_user.subscribed = False
            simple_user.unsubscribed_at = datetime.utcnow()
            user = User.query.filter_by(
                simple_user_id=int(simple_user_id)
            )
            user.subscribed = False
            user.unsubscribed_at = datetime.utcnow()
            db.session.commit()
            return {
                "message": f"{simple_user.email} successfully unsubscribed!",
            }, 200
        except ValueError as ve:
            return {
                "message": f"Value Error: {ve}",
            }, 404
        except exc.IntegrityError as ie:
            db.session.rollback()
            return {
                "message": f"Integrity Error: {ie}"
            }, 400


class GetUsers(Resource):
    def get(self):
        """
        Get all users.
        """
        return {
            "users": [user.to_dict() for user in User.query.all()]
        }, 200


class GetUser(Resource):
    def get(self, user_id):
        """
        Get single user details.
        """
        try:
            user = User.query.filter_by(id=int(user_id)).first()
            if not user:
                return {
                    "message": "User does not exist."
                }, 404
            return {
                "user": user.to_dict()
            }, 200
        except ValueError as ve:
            return {
                "message": f"Value Error: {ve}."
            }, 404


# class Signup(Resource):
#     def post(self):
#         post_data = request.get_json()
#         if not post_data:
#             return {
#                 "message": "Invalid payload."
#             }, 400
#         try:
#             username = post_data["username"]
#             email = post_data["email"]
#             if not validate_email(email):
#                 return {
#                     "message": f"{email} is not a valid email."
#                 }
#             if User.query.filter_by(email=email).first():
#                 return {
#                     "message": f"User {email} already exists."
#                 }, 400
#             elif User.query.filter_by(username=username).first():
#                 return {
#                     "message": f"User {username} already exists."
#                 }, 400
#             simple_user = SimpleUser.query.filter_by(email=email).first()
#             if simple_user:
#                 simple_user.signed_up = True
#             else:
#                 simple_user = SimpleUser(email=email, signed_up=True)
#                 db.session.add(simple_user)
#                 db.session.commit()
#             post_data["simple_user_id"] = simple_user.id

#             new_address = Address(**post_data["address"])
#             db.session.add(new_address)
#             db.session.commit()
#             post_data["main_address_id"] = new_address.id
#             del post_data["address"]

#             post_data["password_hash"] = post_data["password"]
#             del post_data["password"]
#             user = User(**post_data)
#             user.set_password_hash(post_data["password_hash"])
#             db.session.add(user)

#             simple_user.user = user
#             user.addresses = [new_address]
#             user.address_history = [new_address.id]

#             db.session.commit()

#             auth_token = user.encode_auth_token(user.id)
#             return {
#                 "status": "success",
#                 "message": f"{username} has signed up!"
#                 "auth_token": auth_token.decode()
#             }, 201
#         except TypeError as te:
#             return {
#                 "message": f"Type Error: {te}"
#             }, 400
#         except KeyError as ke:
#             return {
#                 "message": f"Key Error: {ke}"
#             }, 400
#         except exc.IntegrityError as ie:
#             db.session.rollback()
#             return {
#                 "message": f"Integrity Error: {ie}"
#             }, 400


class Delete(Resource):
    def get(self, user_id):
        """
        Get single simple_user details.
        """
        try:
            user = User.query.filter_by(
                id=int(user_id)
            ).first()
            if not user:
                return {
                    "message": f"User id {user_id} does not exist.",
                }, 404
            user.deleted = False
            user.delted_at = datetime.utcnow
            db.session.commit()
            return {
                "message": f"{user.email} successfully deleted!",
            }, 200
        except ValueError as ve:
            return {
                "message": f"Value Error: {ve}",
            }, 404
        except exc.IntegrityError as ie:
            db.session.rollback()
            return {
                "message": f"Integrity Error: {ie}"
            }, 400


api.add_resource(Ping, "/users/ping")
api.add_resource(SimpleUsers, "/users/simple")
api.add_resource(GetSimpleUser, "/users/simple/<simple_user_id>")
api.add_resource(Subscribe, "/users/subscribe")
api.add_resource(Unsubscribe, "/users/unsubscribe/<simple_user_id>")
api.add_resource(GetUsers, "/users")
api.add_resource(GetUser, "/users", "/users/<user_id>")
#api.add_resource(Signup, "/auth/signup")
#api.add_resource(Signup, "/users/signup")
api.add_resource(Delete, "/users/delete/<simple_user_id>")
