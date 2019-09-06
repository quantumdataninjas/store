from datetime import datetime
import re
from project import db
# from project.api.models.simple_user import SimpleUser
# from project.api.models.user import User
# from project.api.models.address import Address
from project.api.models import (
    SimpleUser,
    User,
    Address,
    UserAddress,
)


simple_user_dict = {"email": "user@test.org"}
simple_user_dict2 = {"email": "user2@test.org"}
user_dict = {
    "username": "user",
    "email": "user@test.org",
    "subscribed": True,
    "terms_and_conditions": True,
    "firstname": "first",
    "middlename": "middle",
    "lastname": "last",
    "address": {
        "address1": "1523 John St",
        "address2": None,
        "city": "Fort Lee",
        "state": "NJ",
        "zipcode": "07024",
        "country": "United States",
    },
    "phone": None,
    "birthday": str(datetime(1990, 1, 1)),
}
user_dict2 = {
    "username": "user2",
    "email": "user2@test.org",
    "subscribed": True,
    "terms_and_conditions": True,
    "firstname": "first",
    "middlename": "middle",
    "lastname": "last",
    "address": {
        "address1": "1523 John St",
        "address2": None,
        "city": "Fort Lee",
        "state": "NJ",
        "zipcode": "07024",
        "country": "United States",
    },
    "phone": None,
    "birthday": str(datetime(1990, 1, 1)),
}


def validate_email(email):
    return re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
        email
    )

def add_simple_user(new_simple_user):
    simple_user = SimpleUser(**new_simple_user)
    db.session.add(simple_user)
    db.session.commit()
    return simple_user


def add_user(new_user):
    simple_user = SimpleUser.query.filter_by(email=new_user["email"]).first()
    if not simple_user:
        simple_user = add_simple_user({"email": new_user["email"]})

    address = Address(**new_user["address"])
    db.session.add(address)
    db.session.commit()
    del new_user["address"]

    new_user["simple_user_id"] = simple_user.id
    new_user["main_address_id"] = address.id

    user = User(**new_user)
    user.addresses = [address]
    user.address_history = [address.id]
    db.session.add(user)

    simple_user.user = user

    db.session.commit()
    return user

