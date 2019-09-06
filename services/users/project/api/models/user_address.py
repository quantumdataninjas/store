from datetime import datetime
from project import db


class UserAddress(db.Model):
    __tablename__ = "user_address"
    user_id = db.Column(
        db.BigInteger, db.ForeignKey("user.id"), primary_key=True
    )
    address_id = db.Column(
        db.BigInteger, db.ForeignKey("address.id"), primary_key=True
    )
    created_at = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "address_id": self.address_id,
            "created_at": str(self.created_at)
        }


class UserAddressHistory(db.Model):
    __tablename__ = "user_address_history"
    user_id = db.Column(
        db.BigInteger, db.ForeignKey("user.id"), primary_key=True
    )
    address_id = db.Column(
        db.BigInteger, db.ForeignKey("address.id"), primary_key=True
    )
    created_at = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=False
    )

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "address_id": self.address_id,
            "created_at": str(self.created_at)
        }
