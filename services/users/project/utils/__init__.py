from datetime import datetime
import re
from flask_mail import Message
from project import mail

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
        print ('mail')
        return 'Mail sent!'
    except Exception as e:
        return(str(e))

simple_user_dict = {"email": "user@test.org"}
simple_user_dict2 = {"email": "user2@test.org"}
user_dict = {
    "email": "user@test.org",
    "subscribed": True,
    "terms_and_conditions": True,
    "firstname": "first",
    "middlename": "middle",
    "lastname": "last",
    "address1": "1523 John St",
    "address2": None,
    "city": "Fort Lee",
    "state": "NJ",
    "zipcode": "07024",
    "country": "United States",
    "phone": None,
    # "birthmonth": "January",
    "birthday": str(datetime(1990, 1, 1)),
    # "birthyear": "1990",
}
user_dict2 = {
    "email": "user2@test.org",
    "subscribed": True,
    "terms_and_conditions": True,
    "firstname": "first",
    "middlename": "middle",
    "lastname": "last",
    "address1": "1523 John St",
    "address2": None,
    "city": "Fort Lee",
    "state": "NJ",
    "zipcode": "07024",
    "country": "United States",
    "phone": None,
    # "birthmonth": "January",
    "birthday": str(datetime(1990, 1, 1)),
    # "birthyear": "1990",
}


def validate_email(email):
    return re.match(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
        email
    )
