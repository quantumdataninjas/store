import time
import json
import unittest
from copy import deepcopy

from project import db
from project.api.models import (
    SimpleUser,
    User
)
from project.tests.base import BaseTestCase
from project.utils import (
    add_user,
    user_dict,
    simple_user_dict
)


class TestAuthBlueprint(BaseTestCase):
    def test_user_can_signup(self):
        """
        Ensure a new user can signup.
        """
        with self.client:
            response = self.client.post(
                "/auth/signup",
                data=json.dumps(user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            user = User.query.filter_by(
                email=user_dict["email"]
            ).first()
            simple_user = SimpleUser.query.filter_by(
                email=user.email
            ).first()
            self.assertEqual(simple_user.signed_up, True)
            self.assertTrue(data['auth_token'])
            self.assertIn(f"{user.username} has signed up!", data["message"])

    def test_subscribed_user_record_updates_after_signup(self):
        """
        Ensure a subscribed user is signedup after signing up.
        """
        with self.client:
            self.client.post(
                "/users/subscribe",
                data=json.dumps(simple_user_dict),
                content_type="application/json",
            )
            simple_user = SimpleUser.query.filter_by(
                email=simple_user_dict["email"]
            ).first()
            self.assertEqual(simple_user.signed_up, False)
            response = self.client.post(
                "/auth/signup",
                data=json.dumps(user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(simple_user.signed_up, True)
            self.assertIn("%s has signed up!" % user_dict["username"], data["message"])

    def test_signup_with_str(self):
        """
        Ensure error is thrown if the Post data is not a JSON object.
        """
        with self.client:
            response = self.client.post(
                "/auth/signup",
                data=json.dumps("not json"),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                "Type Error: string indices must be integers",
                data["message"]
            )

    def test_signup_with_empty_json(self):
        """
        Ensure error is thrown if the JSON object is empty.
        """
        with self.client:
            response = self.client.post(
                "/auth/signup",
                data=json.dumps({}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])

    def test_signup_with_invalid_json(self):
        """
        Ensure error is thrown if simple_user object is posted.
        """
        with self.client:
            response = self.client.post(
                "/auth/signup",
                data=json.dumps(simple_user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Key Error: 'username'", data["message"])

    def test_signup_with_invalid_email(self):
        """
        Ensure error is thrown if the email is invalid.
        """
        with self.client:
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps({**user_dict, "email": "invalid"}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("invalid is not a valid email.", data["message"])

    def test_signup_with_duplicate_email(self):
        """
        Ensure error is thrown if the email already exists.
        """
        with self.client:
            self.client.post(
                "/auth/signup",
                data=json.dumps(user_dict),
                content_type="application/json",
            )
            response = self.client.post(
                "/auth/signup",
                data=json.dumps(user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                f'User {user_dict["email"]} already exists.',
                data["message"],
            )
    

    def test_signed_up_user_signin(self):
        with self.client:
            add_user(deepcopy(user_dict))
            response = self.client.post(
                '/auth/signin',
                data=json.dumps(user_dict),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['message'] == 'Successfully signed in.')
            self.assertTrue(data['auth_token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_not_signed_up_user_signin(self):
        with self.client:
            response = self.client.post(
                '/auth/signin',
                data=json.dumps(user_dict),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            email = user_dict["email"]
            self.assertTrue(data['message'] == f'User {email} does not exist.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)

    def test_valid_signout(self):
        add_user(deepcopy(user_dict))
        with self.client:
            resp_login = self.client.post(
                '/auth/signin',
                data=json.dumps(user_dict),
                content_type='application/json'
            )
            token = json.loads(resp_login.data.decode())['auth_token']
            response = self.client.get(
                '/auth/signout',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['message'] == 'Successfully signed out.')
            self.assertEqual(response.status_code, 200)

    def test_invalid_signout_expired_token(self):
        add_user(deepcopy(user_dict))
        with self.client:
            resp_login = self.client.post(
                '/auth/signin',
                data=json.dumps(user_dict),
                content_type='application/json'
            )
            time.sleep(4)
            token = json.loads(resp_login.data.decode())['auth_token']
            response = self.client.get(
                '/auth/signout',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertTrue(
                data['message'] == 'Signature expired. Please sign in again.'
            )
            self.assertEqual(response.status_code, 401)

    def test_invalid_signout(self):
        with self.client:
            response = self.client.get(
                '/auth/signout',
                headers={'Authorization': 'Bearer invalid'}
            )
            data = json.loads(response.data.decode())
            self.assertTrue(
                data['message'] == 'Invalid token. Please sign in again.'
            )
            self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()