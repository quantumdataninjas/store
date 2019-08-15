import json
import unittest
from project import (
    db, new_simple_user_dict, new_simple_user_dict2,
    new_user_dict, new_user_dict2
)
from project.api.models import SimpleUser, User
from project.tests.base import BaseTestCase


def add_simple_user(new_simple_user_dict):
    new_simple_user = SimpleUser(email=new_simple_user_dict['email'])
    db.session.add(new_simple_user)
    db.session.commit()
    return new_simple_user

def add_user(new_user_dict):
    new_user = User(**new_user_dict)
    db.session.add(new_user)
    db.session.commit()
    return new_user


class TestUsersService(BaseTestCase):
    """Tests for the Users Service."""


    def test_get_users_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])

    def test_user_can_subscribe(self):
        """Ensure a new user can subscribe for emails."""
        with self.client:
            response = self.client.post(
                '/users/subscribe',
                data=json.dumps(new_simple_user_dict),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            new_simple_user = SimpleUser.query.filter_by(email=new_simple_user_dict['email']).first()
            self.assertEqual(new_simple_user_dict['email'], new_simple_user.email)
            self.assertIn(f'{new_simple_user.email} is subscribed!', data['message'])

    def test_user_can_register(self):
        """Ensure a new user can register"""
        with self.client:
            response = self.client.post(
                '/users/register',
                data=json.dumps(new_user_dict),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            new_user = User.query.filter_by(email=new_user_dict['email']).first()
            self.assertEqual(new_user_dict['email'], new_user.email)
            new_simple_user = SimpleUser.query.filter_by(email=new_user.email).first()
            self.assertEqual(new_simple_user.registered, True)
            self.assertIn(f'{new_user.email} is registered!', data['message'])

    def test_subscribed_user_record_updates_after_registering(self):
        """Ensure a subscribed user is registered after registering"""
        with self.client:
            self.client.post(
                '/users/subscribe',
                data=json.dumps(new_simple_user_dict),
                content_type='application/json'
            )
            new_simple_user = SimpleUser.query.filter_by(email=new_simple_user_dict['email']).first()
            self.assertEqual(new_simple_user.registered, False)
            response = self.client.post(
                '/users/register',
                data=json.dumps(new_user_dict),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(new_simple_user.registered, True)

    def test_subscribe_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                '/users/subscribe',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])

    def test_register_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                '/users/register',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])

    def test_subscribe_user_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object does not have an email key."""
        with self.client:
            response = self.client.post(
                '/users/subscribe',
                data=json.dumps({'username':'test'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Integrity Error:', data['message'])

    def test_register_user_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object does not have a email key."""
        with self.client:
            response = self.client.post(
                '/users/register',
                data=json.dumps(new_simple_user_dict),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Integrity Error:', data['message'])

    def test_subscribe_user_duplicate_email(self):
        """Ensure error is thrown if the email already exists."""
        with self.client:
            self.client.post(
                '/users/subscribe',
                data=json.dumps(new_simple_user_dict),
                content_type='application/json',
            )
            response = self.client.post(
                '/users/subscribe',
                data=json.dumps(new_simple_user_dict),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                f'User {new_simple_user_dict["email"]} is already subscribed.', data['message'])

    def test_register_user_duplicate_email(self):
        """Ensure error is thrown if the email already exists."""
        with self.client:
            self.client.post(
                '/users/register',
                data=json.dumps(new_user_dict),
                content_type='application/json',
            )
            response = self.client.post(
                '/users/register',
                data=json.dumps(new_user_dict),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                f'User {new_user_dict["email"]} already exists.', data['message'])

    def test_get_simple_user(self):
        """Ensure get single user behaves correctly."""
        new_simple_user = add_simple_user(new_simple_user_dict)
        with self.client:
            response = self.client.get(f'/users/simple/{new_simple_user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(new_simple_user.email, data['data']['email'])

    def test_get_simple_user_with_string(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get('/users/simple/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Value Error:', data['message'])

    def test_get_simple_user_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client:
            response = self.client.get('/users/simple/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist.', data['message'])

    def test_get_user(self):
        """Ensure get single user behaves correctly."""
        new_user = add_user(new_user_dict)
        with self.client:
            response = self.client.get(f'/users/{new_user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn(new_user.email, data['data']['email'])

    def test_get_user_with_string(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get('/users/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Value Error:', data['message'])

    def test_get_user_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist.', data['message'])

    def test_get_all_simple_users(self):
        """Ensure get all simple users behaves correctly."""
        add_simple_user(new_simple_user_dict)
        add_simple_user(new_simple_user_dict2)
        with self.client:
            response = self.client.get('/users/simple')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['simple_users']), 2)
            self.assertIn('user@test.org', data['data']['simple_users'][0]['email'])
            self.assertIn('user2@test.org', data['data']['simple_users'][1]['email'])

    def test_get_all_users(self):
        """Ensure get all users behaves correctly."""
        add_user(new_user_dict)
        add_user(new_user_dict2)
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('user@test.org', data['data']['users'][0]['email'])
            self.assertIn('user2@test.org', data['data']['users'][1]['email'])


if __name__ == '__main__':
    unittest.main()
