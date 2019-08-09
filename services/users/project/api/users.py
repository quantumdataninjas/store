from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc
from project import db
from project.api.models import SimpleUser, User


users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }


class UsersSubscribe(Resource):
    def post(self):
        post_data = request.get_json()
        if not post_data:
            return {
                'status': 'fail',
                'message': 'Invalid payload.'
            }, 400
        email = post_data.get('email')
        try:
            simple_user = SimpleUser.query.filter_by(email=email).first()
            if not simple_user:
                db.session.add(SimpleUser(email=email, subscribed=True))
                db.session.commit()
                return {
                    'status': 'success',
                    'message': f'{email} is subscribed!'
                }, 201
            else:
                return {
                    'status': 'fail',
                    'message': f'User {email} is already subscribed.'
                }, 400
        except exc.IntegrityError:
            db.session.rollback()
            return {
                'status': 'fail',
                'message': 'Invalid payload.'
            }, 400


class UsersRegister(Resource):
    def post(self):
        post_data = request.get_json()
        if not post_data:
            return {
                'status': 'fail',
                'message': 'Invalid payload.'
            }, 400
        email = post_data.get('email')
        subscribed = post_data.get('subscribed')
        terms_and_conditions = post_data.get('terms_and_conditions')
        firstname = post_data.get('firstname')
        middlename = post_data.get('middlename')
        lastname = post_data.get('lastname')
        address1 = post_data.get('address1')
        address2 = post_data.get('address2')
        city = post_data.get('city')
        state = post_data.get('state')
        zipcode = post_data.get('zipcode')
        country = post_data.get('country')
        phone = post_data.get('phone')
        birthmonth = post_data.get('birthmonth')
        birthday = post_data.get('birthday')
        birthyear = post_data.get('birthyear')
        try:
            user = User.query.filter_by(email=email).first()
            if not user:
                db.session.add(
                    User(
                        email=email,
                        subscribed=subscribed,
                        terms_and_conditions=terms_and_conditions,
                        firstname=firstname,
                        middlename=middlename,
                        lastname=lastname,
                        address1=address1,
                        address2=address2,
                        city=city,
                        state=state,
                        zipcode=zipcode,
                        country=country,
                        phone=phone,
                        birthmonth=birthmonth,
                        birthday=birthday,
                        birthyear=birthyear
                    )
                )
                simple_user = SimpleUser.query.filter_by(email=email).first()
                if simple_user:
                    simple_user.registered = True
                else:
                    db.session.add(
                        SimpleUser(
                            email=email,
                            subscribed=subscribed,
                            registered=True
                        )
                    )
                db.session.commit()
                return {
                    'status': 'success',
                    'message': f'{email} is registered!'
                }, 201
            else:
                return {
                    'status': 'fail',
                    'message': f'User {email} already exists.'
                }, 400
        except exc.IntegrityError:
            db.session.rollback()
            return {
                'status': 'fail',
                'message': 'Invalid payload.'
            }, 400


api.add_resource(UsersPing, '/users/ping')
api.add_resource(UsersSubscribe, '/users/subscribe')
api.add_resource(UsersRegister, '/users/register')
