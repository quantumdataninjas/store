import sys
import unittest
import coverage
# from flask.cli import FlaskGroup
from project import create_app, db
from project.utils import(
    simple_user_dict, simple_user_dict2,
    user_dict, user_dict2
)
from project.api.models import SimpleUser, User


COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app()
# cli = FlaskGroup(create_app=create_app)

@app.cli.command("cov")
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


@app.cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@app.cli.command("seed_db")
def seed_db():
    """Seeds the database."""
    db.session.add(SimpleUser(**simple_user_dict))
    db.session.add(SimpleUser(**simple_user_dict2))
    db.session.add(User(**user_dict))
    db.session.add(User(**user_dict2))
    db.session.commit()

@app.cli.command("test")
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


# if __name__ == '__main__':
    # app.run()
    # cli()
