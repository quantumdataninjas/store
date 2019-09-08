from copy import deepcopy
import unittest
from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.utils import (
    add_user,
    user_dict,
    user_dict2
)
from sqlalchemy.exc import IntegrityError


class TestSimpleUserModel(BaseTestCase):

    def test_add_simple_user(self):
        user = add_user(deepcopy(user_dict))
        self.assertTrue(user.id)
        self.assertEqual(user.email, 'user@test.org')
        self.assertTrue(user.online)

    def test_add_user_duplicate_email(self):
        user_copy = deepcopy(user_dict)
        add_user(user_copy)
        duplicate_user = User(**user_copy)
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_dict(self):
      user = add_user(deepcopy(user_dict))
      self.assertTrue(isinstance(user.to_dict(), dict))

    def test_passwords_are_random(self):
        user1 = add_user(deepcopy(user_dict))
        user2 = add_user(deepcopy(user_dict2))
        self.assertNotEqual(user1.password_hash, user2.password_hash)


if __name__ == '__main__':
    unittest.main()
