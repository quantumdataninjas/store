from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
from sqlalchemy import exc, or_
from project.api.models import (
    SimpleUser,
    User,
    Address
)
from project import db, argon2
from project.utils import validate_email

auth_blueprint = Blueprint('auth', __name__)
api = Api(auth_blueprint)


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


class Signup(Resource):
    """
    Signup Api
    """

    def post(self):
        post_data = request.get_json()
        if not post_data:
            return {
                "message": "Invalid payload."
            }, 400
        try:
            print('enter getJSONResult', flush=True)

            username = post_data["username"]
            email = post_data["email"]
            if not validate_email(email):
                return {
                    "message": f"{email} is not a valid email."
                }, 400
            if User.query.filter_by(email=email).first():
                return {
                    "message": f"User {email} already exists."
                }, 400
            elif User.query.filter_by(username=username).first():
                return {
                    "message": f"User {username} already exists."
                }, 400
            simple_user = SimpleUser.query.filter_by(email=email).first()
            if simple_user:
                simple_user.signed_up = True
            else:
                simple_user = SimpleUser(email=email, signed_up=True)
                db.session.add(simple_user)
                db.session.commit()
            post_data["simple_user_id"] = simple_user.id


            print('enter getJSONResult', flush=True)

            new_address = Address(**post_data["address"])

            print('enter getJSONResult', flush=True)
            db.session.add(new_address)
            db.session.commit()


            post_data["main_address_id"] = new_address.id
            del post_data["address"]



            post_data["password_hash"] = post_data["password"]
            del post_data["password"]
            user = User(**post_data)
            user.set_password_hash(post_data["password_hash"])
            db.session.add(user)

            simple_user.user = user
            user.addresses = [new_address]
            user.address_history = [new_address.id]

            db.session.commit()

            auth_token = user.encode_auth_token(user.id)
            return {
                "message": f"{username} has signed up!",
                "auth_token": auth_token.decode()
            }, 201
        except TypeError as te:
            return {
                "message": f"Type Error: {te}"
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


#@auth_blueprint.route('/auth/login', methods=['POST']) #todo delete
class Signin(Resource):
    """
    Signin Api
    """

    def post(self):
        post_data = request.get_json()
        if not post_data:
            return {
                "message": "Invalid payload."
            }
        email = post_data["email"]
        password = post_data["password"]
        try:
            user = User.query.filter_by(email=email).first()
            # if user and bcrypt.check_password_hash(user.password_hash, password)
            if user and argon2.check_password_hash(user.password_hash, password):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    return {
                        "message": "Successfully signed in.",
                        "auth_token": auth_token.decode()
                    }, 200
            return {
                "message": f"User {email} does not exist."
            }, 404
        except Exception as e:
            return {
                "message": f"Exception: {e}"
            }, 500

class Signout(Resource):
    """
    Signout API
    """

    def get(self):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return {
                "message": "Provide a valid auth token."
            }, 403
        auth_token = auth_header.split(" ")[1]
        resp = User.decode_auth_token(auth_token)
        if isinstance(resp, str):
            return {
                "message": resp
            }, 401
        return {
            "message": "Successfully signed out."
        }, 200


api.add_resource(Ping, "/users/auth/ping")
api.add_resource(Signup, "/users/auth/signup")
api.add_resource(Signin, "/users/auth/signin")
