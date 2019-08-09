import json
import unittest
from project.api.models import SimpleUser, User
from project.tests.base import BaseTestCase


new_simple_user_dict = {'email': 'user@test.org'}
new_user_dict = {
    'email': 'user@test.org',
    'subscribed': True,
    'terms_and_conditions': True,
    'firstname': 'first',
    'middlename': 'middle',
    'lastname': 'last',
    'address1': '1523 John St',
    'city': 'Fort Lee',
    'state': 'NJ',
    'zipcode': '07024',
    'country': 'United States',
    'birthmonth': 'January',
    'birthday': '01',
    'birthyear': '1990'
}

class TestUsersService(BaseTestCase):
    """Tests for the Users Service."""


    def test_users(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

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
            self.assertIn('success', data['status'])

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
            self.assertIn('success', data['status'])

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
            self.assertIn('success', data['status'])

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
            self.assertIn('fail', data['status'])

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
            self.assertIn('fail', data['status'])

    def test_register_user_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object does not have a username key."""
        with self.client:
            response = self.client.post(
                '/users/register',
                data=json.dumps(new_simple_user_dict),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

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
            self.assertIn('fail', data['status'])

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
            self.assertIn('fail', data['status'])


if __name__ == '__main__':
    unittest.main()
