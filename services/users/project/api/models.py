from datetime import datetime
from project import db


class SimpleUser(db.Model):
    __tablename__ = "simple_users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    # ip = db.Column(db.String(15), nullable=False)
    subscribed = db.Column(db.Boolean(), default=True, nullable=False)
    signed_up = db.Column(db.Boolean(), default=False, nullable=False)
    online = db.Column(db.Boolean(), default=True, nullable=False)
    last_signin = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )
    last_signout = db.Column(db.DateTime, index=True, nullable=True)
    created_at = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )

    def __repr__(self):
        return "<SimpleUser {}>".format(self.email)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "subscribed": self.subscribed,
            "signed_up": self.signed_up,
            "online": self.online,
            "last_signin": str(self.last_signin),
            "last_signout": str(self.last_signout),
            "created_at": str(self.created_at),
        }


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    # ip = db.Column(db.String(15), nullable=False)
    subscribed = db.Column(db.Boolean(), default=True, nullable=False)
    terms_and_conditions = db.Column(
        db.Boolean(), default=False, nullable=False
    )
    # verified = db.Column(db.Boolean(), default=False, nullable=False)
    # hash = db.Column(db.String(128), nullable=False)
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
    last_signin = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )
    last_signout = db.Column(db.DateTime, index=True, nullable=True)
    created_at = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=True
    )

    def __repr__(self):
        return "<User {}>".format(self.email)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "subscribed": self.subscribed,
            "terms_and_conditions": self.terms_and_conditions,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "address1": self.address1,
            "address2": self.address2,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "country": self.country,
            "phone": self.phone,
            "birthmonth": self.birthmonth,
            "birthday": self.birthday,
            "birthyear": self.birthyear,
            "online": self.online,
            "last_signin": str(self.last_signin),
            "last_signout": str(self.last_signout),
            "created_at": str(self.created_at),
        }
