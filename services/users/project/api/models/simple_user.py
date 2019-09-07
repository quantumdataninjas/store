<<<<<<< HEAD
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
        db.DateTime, default=datetime.utcnow, nullable=False
    )
    last_signout = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )
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
||||||| merged common ancestors
=======
from datetime import datetime
from project import db


class SimpleUser(db.Model):
    __tablename__ = "simple_users"
    id = db.Column(
        db.BigInteger, primary_key=True, autoincrement=True
    )
    email = db.Column(
        db.String(128), index=True, unique=True, nullable=False
    )
    # ip = db.Column(
    #     db.String(15), nullable=False
    # )
    subscribed = db.Column(
        db.Boolean, default=True, nullable=False
    )
    signed_up = db.Column(
        db.Boolean, default=False, nullable=False
    )
    online = db.Column(
        db.Boolean, default=True, nullable=False
    )
    last_signin = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )
    last_signout = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False
    )
    unsubscribed_at = db.Column(
        db.DateTime, index=True, nullable=True
    )
    created_at = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )

    def __repr__(self):
        return f"<SimpleUser {self.email}>"

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "subscribed": self.subscribed,
            "signed_up": self.signed_up,
            "online": self.online,
            "last_signin": str(self.last_signin),
            "last_signout": str(self.last_signout),
            "unsubscribed_at": str(self.unsubscribed_at),
            "created_at": str(self.created_at),
        }
>>>>>>> 66ad30331d8b93be03074765d0c642358ca2a11b
