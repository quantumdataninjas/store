import unittest
from project import db
from project.api.models import SimpleUser
from project.tests.base import BaseTestCase
from project.utils import (
    add_simple_user,
    simple_user_dict,
    simple_user_dict2
)
from sqlalchemy.exc import IntegrityError


class TestSimpleUserModel(BaseTestCase):

    def test_add_simple_user(self):
        user = add_simple_user(simple_user_dict)
        self.assertTrue(user.id)
        self.assertEqual(user.email, 'user@test.org')
        self.assertTrue(user.online)

    def test_add_user_duplicate_email(self):
        add_simple_user(simple_user_dict)
        duplicate_user = SimpleUser(**simple_user_dict)
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_dict(self):
      user = add_simple_user(simple_user_dict)
      self.assertTrue(isinstance(user.to_dict(), dict))


if __name__ == '__main__':
    unittest.main()