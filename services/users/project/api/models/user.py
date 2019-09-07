from datetime import datetime
# from sqlalchemy.ext.associationproxy import association_proxy
# from bcrypt import generate_password_hash
from project import db, bcrypt
# from project.bcrypt import generate_password_hash
# from .user_address import UserAddress, UserAddressHistory


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(
        db.BigInteger, primary_key=True, autoincrement=True
    )
    simple_user_id = db.Column(
        db.BigInteger, db.ForeignKey("simple_users.id"), nullable=False
    )
    username = db.Column(
        db.String(30), index=True, unique=True, nullable=False
    )
    email = db.Column(
        db.String(128), index=True, unique=True, nullable=False
    )
    password_hash = db.Column(
        db.String(255), nullable=False
    )
    # ip = db.Column(
    #     db.String(15), index=True, nullable=False
    # )
    subscribed = db.Column(
        db.Boolean, default=True, nullable=False
    )
    terms_and_conditions = db.Column(
        db.Boolean, default=False, nullable=False
    )
    verified = db.Column(
        db.Boolean, default=False, nullable=False
    )
    # hash = db.Column(
    #     db.String(128), nullable=False
    # )
    firstname = db.Column(
        db.String(128), nullable=False
    )
    middlename = db.Column(
        db.String(128), nullable=True
    )
    lastname = db.Column(
        db.String(128), nullable=False
    )
    main_address_id = db.Column(
        db.BigInteger, db.ForeignKey("addresses.id"), nullable=False
    )
    # TODO: check null address
    # addresses = db.relationship(
    #     "Address", primaryjoin="and_(User.main_address_id==Address.id)",
    #     "Address",
    #     primaryjoin="and_(User.main_address_id==Address.id)",
    #     back_populates="user",
    # )
    addresses = db.relationship(
        "Address", secondary="user_addresses", backref="users", lazy=True
    )
    # addresses = association_proxy(
    #     "user_addresses",
    #     "address",
    #     creator=lambda address: UserAddress(address=address)
    # )
    address_history = db.Column(
        db.ARRAY(db.BigInteger), default=[], nullable=False
    )
    # address_history = db.relationship(
    #     "Address", secondary="user_address_history", backref="user", lazy=True
    # )
    phone = db.Column(
        db.String(20), unique=True, nullable=True
    )
    birthday = db.Column(
        db.DateTime, nullable=False
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
    created_at = db.Column(
        db.DateTime, index=True, default=datetime.utcnow, nullable=True
    )
    deleted = db.Column(
        db.Boolean, default=False, nullable=False
    )
    deleted_at = db.Column(
        db.DateTime, index=True, nullable=True
    )
    unsubscribed_at = db.Column(
        db.DateTime, index=True, nullable=True
    )
    
    def set_password_hash(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "simple_user_id": self.simple_user_id,
            "username": self.username,
            "email": self.email,
            # TODO: hash password
            "password_hash": self.password_hash,
            "subscribed": self.subscribed,
            "terms_and_conditions": self.terms_and_conditions,
            "verified": self.verified,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "main_address_id": self.main_address_id,
            "addresses": [address.to_dict() for address in self.addresses],
            "address_history": self.address_history,
            # "address_history": [address.to_dict() for address in self.address_history],
            "phone": self.phone,
            "birthday": str(self.birthday),
            "online": self.online,
            "last_signin": str(self.last_signin),
            "last_signout": str(self.last_signout),
            "created_at": str(self.created_at),
            "deleted": self.deleted,
            "deleted_at": str(self.deleted_at)
        }