from datetime import datetime
from sqlalchemy.sql import func
from project import db


class SimpleUser(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    # ip = db.Column(db.String(15), nullable=False)
    subscribed = db.Column(db.Boolean(), default=True, nullable=False)
    registered = db.Column(db.Boolean(), default=False, nullable=False)
    online = db.Column(db.Boolean(), default=True, nullable=False)
    lastlogin = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    lastlogout = db.Column(db.DateTime, index=True, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)

    def __init__(self, email, subscribed=True, registered=False):
        self.email = email
        self.subscribed = subscribed
        self.registered = registered

    def __repr__(self):
        return '<Email {}>'.format(self.email)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    # ip = db.Column(db.String(15), nullable=False)
    subscribed = db.Column(db.Boolean(), default=True, nullable=False)
    terms_and_conditions = db.Column(db.Boolean(), default=False, nullable=False)
    verified = db.Column(db.Boolean(), default=False, nullable=False)
    firstname = db.Column(db.String(128), nullable=False)
    middlename = db.Column(db.String(128), nullable=True)
    lastname = db.Column(db.String(128), nullable=False)
    address1 = db.Column(db.String(128), nullable=False)
    address2 = db.Column(db.String(128), nullable=True)
    city = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipcode = db.Column(db.String(15), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=True)
    birthmonth = db.Column(db.String(10), nullable=False)
    birthday = db.Column(db.String(2), nullable=False)
    birthyear = db.Column(db.String(4), nullable=False)
    online = db.Column(db.Boolean(), default=True, nullable=False)
    lastlogin = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    lastlogout = db.Column(db.DateTime, index=True, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=True)

    def __init__(self, email, subscribed, terms_and_conditions, firstname, middlename, lastname, address1, address2, city, state, zipcode, country, phone, birthmonth, birthday, birthyear):
        self.email = email
        self.subscribed = subscribed
        self.terms_and_conditions = terms_and_conditions
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
        self.phone = phone
        self.birthmonth = birthmonth
        self.birthday = birthday
        self.birthyear = birthyear

    def __repr__(self):
        return '<User {}>'.format(self.email)
