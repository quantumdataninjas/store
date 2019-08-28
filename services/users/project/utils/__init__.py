from datetime import datetime
import re


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
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)