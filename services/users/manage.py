import sys
import unittest
from flask.cli import FlaskGroup
from project import (
    create_app, db,
    new_simple_user_dict, new_simple_user_dict2,
    new_user_dict, new_user_dict2
)
from project.api.models import SimpleUser, User


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    SimpleUser.create_all()
    User.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(SimpleUser(
        email=new_simple_user_dict["email"]
    ))
    db.session.add(SimpleUser(
        email=new_simple_user_dict2["email"]
    ))
    db.session.add(User(
        email=new_user_dict["email"],
        subscribed=new_user_dict["subscribed"],
        terms_and_conditions=new_user_dict["terms_and_conditions"],
        firstname=new_user_dict["firstname"],
        middlename=new_user_dict["middlename"],
        lastname=new_user_dict["lastname"],
        address1=new_user_dict["address1"],
        address2=new_user_dict["address2"],
        city=new_user_dict["city"],
        state=new_user_dict["state"],
        zipcode=new_user_dict["zipcode"],
        country=new_user_dict["country"],
        phone=new_user_dict["phone"],
        birthmonth=new_user_dict["birthmonth"],
        birthday=new_user_dict["birthday"],
        birthyear=new_user_dict["birthyear"]
    ))
    db.session.add(User(
        email=new_user_dict2["email"],
        subscribed=new_user_dict2["subscribed"],
        terms_and_conditions=new_user_dict2["terms_and_conditions"],
        firstname=new_user_dict2["firstname"],
        middlename=new_user_dict2["middlename"],
        lastname=new_user_dict2["lastname"],
        address1=new_user_dict2["address1"],
        address2=new_user_dict2["address2"],
        city=new_user_dict2["city"],
        state=new_user_dict2["state"],
        zipcode=new_user_dict2["zipcode"],
        country=new_user_dict2["country"],
        phone=new_user_dict2["phone"],
        birthmonth=new_user_dict2["birthmonth"],
        birthday=new_user_dict2["birthday"],
        birthyear=new_user_dict2["birthyear"]
    ))
    db.session.commit()

@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()
