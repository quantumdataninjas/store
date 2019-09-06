from datetime import datetime
from project import db


class UserAddress(db.Model):
    __tablename__ = "user_addresses"
    users_id = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), primary_key=True
    )
    addresses_id = db.Column(
        db.BigInteger, db.ForeignKey("addresses.id"), primary_key=True
    )
    created_at = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )

    def to_dict(self):
        return {
            "users_id": self.users_id,
            "addresses_id": self.addresses_id,
            "created_at": str(self.created_at)
        }


class UserAddressHistory(db.Model):
    __tablename__ = "user_address_history"
    user_id = db.Column(
        db.BigInteger, db.ForeignKey("users.id"), primary_key=True
    )
    address_id = db.Column(
        db.BigInteger, db.ForeignKey("addresses.id"), primary_key=True
    )
    created_at = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )

    def to_dict(self):
        return {
            "users_id": self.users_id,
            "addresses_id": self.addresses_id,
            "created_at": str(self.created_at)
        }
