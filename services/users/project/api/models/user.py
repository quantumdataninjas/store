from datetime import datetime
from project import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    # ip = db.Column(db.String(15), index=True, nullable=False)
    subscribed = db.Column(db.Boolean(), default=True, nullable=False)
    terms_and_conditions = db.Column(
        db.Boolean(), default=False, nullable=False
    )
    verified = db.Column(db.Boolean(), default=False, nullable=False)
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
    birthday = db.Column(db.DateTime, nullable=False)
    online = db.Column(db.Boolean(), default=True, nullable=False)
    last_signin = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )
    last_signout = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )
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
            "verified": self.verified,
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
            "birthday": str(self.birthday),
            "online": self.online,
            "last_signin": str(self.last_signin),
            "last_signout": str(self.last_signout),
            "created_at": str(self.created_at),
        }
