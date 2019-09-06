from datetime import datetime
from project import db

class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(
        db.BigInteger, primary_key=True, autoincrement=True
    )
    users = db.relationship(
        "User", secondary="user_address", backref="address", lazy=True
    )
    # users_history = db.relationship(
    #     "User", secondary="user_address_history", backref="address", lazy=True
    # )
    # users_history = db.Column(
    #     db.ARRAY(db.BigInteger), nullable=False
    # )
    address1 = db.Column(
        db.String(128), nullable=False
    )
    address2 = db.Column(
        db.String(128), nullable=True
    )
    city = db.Column(
        db.String(128), nullable=False
    )
    state = db.Column(
        db.String(2), nullable=False
    )
    zipcode = db.Column(
        db.String(15), nullable=False
    )
    country = db.Column(
        db.String(30), nullable=False
    )
    created_at = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )
    # deleted = db.Column(
    #     db.Bool, default=False, nullable=False
    # )
    # deleted_at = db.Column(
    #     db.DateTime, index=True, nullable=True
    # )

    def __repr__(self):
        return f"<Address {self.address1} {self.city} {self.state}>"

    def to_dict(self):
        return {
            "id": self.id,
            # "user_id": self.user_id,
            "address1": self.address1,
            "address2": self.address2,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "country": self.country,
            "created_at": str(self.created_at),
            # "deleted_at": str(self.deleted_at),
        }