from datetime import datetime
import re
from flask_mail import Message
from project import db, mail
from project.api.models import (
    SimpleUser,
    User,
    Address,
    UserAddress,
)

simple_user_dict = {"email": "user@test.org"}
simple_user_dict2 = {"email": "user2@test.org"}
user_dict = {
    "simple_user_id": 1,
    "username": "user",
    "email": "user@test.org",
    "password": "password",
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
    "simple_user_id": 2,
    "username": "user2",
    "email": "user2@test.org",
    "password": "password",
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

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

#@app.route('/send-mail/')
def send_test_email():
    try:
        msg = Message("Send Mail Tutorial!",
            sender="hardheadhacker@gmail.com",
            recipients=["hardheadhack@gmail.com"])
        msg.body = "Yo!\nHave you heard the good word of Python???"
        msg.html = '<h1>HTML body</h1>'
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return(str(e))

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

    new_user["password_hash"] = new_user["password"]
    del new_user["password"]

    user = User(**new_user)
    user.set_password_hash(new_user["password_hash"])
    user.addresses = [address]
    user.address_history = [address.id]
    db.session.add(user)

    simple_user.user = user

    db.session.commit()
    return user
