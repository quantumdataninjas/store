import json
import unittest
from project import (
    db,
    new_simple_user_dict,
    new_user_dict,
)
from project.api.models import SimpleUser, User
from project.tests.base import BaseTestCase


def add_simple_user(new_simple_user_dict):
    new_simple_user = SimpleUser(email=new_simple_user_dict["email"])
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
        response = self.client.get("/users/ping")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("pong!", data["message"])

    def test_user_can_subscribe(self):
        """Ensure a new user can subscribe for emails."""
        with self.client:
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps(new_simple_user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            new_simple_user = SimpleUser.query.filter_by(
                email=new_simple_user_dict["email"]
            ).first()
            self.assertEqual(
                new_simple_user_dict["email"], new_simple_user.email
            )
            self.assertIn(
                f"{new_simple_user.email} is subscribed!", data["message"]
            )

    def test_user_can_register(self):
        """Ensure a new user can register"""
        with self.client:
            response = self.client.post(
                "/users/register",
                data=json.dumps(new_user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            new_user = User.query.filter_by(
                email=new_user_dict["email"]
            ).first()
            self.assertEqual(new_user_dict["email"], new_user.email)
            new_simple_user = SimpleUser.query.filter_by(
                email=new_user.email
            ).first()
            self.assertEqual(new_simple_user.registered, True)
            self.assertIn(f"{new_user.email} is registered!", data["message"])

    def test_subscribed_user_record_updates_after_registering(self):
        """Ensure a subscribed user is registered after registering"""
        with self.client:
            self.client.post(
                "/users/subscribe",
                data=json.dumps(new_simple_user_dict),
                content_type="application/json",
            )
            new_simple_user = SimpleUser.query.filter_by(
                email=new_simple_user_dict["email"]
            ).first()
            self.assertEqual(new_simple_user.registered, False)
            response = self.client.post(
                "/users/register",
                data=json.dumps(new_user_dict),
                content_type="application/json",
            )
            # data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(new_simple_user.registered, True)

    def test_subscribe_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps({}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])

    def test_register_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                "/users/register",
                data=json.dumps({}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])

    def test_subscribe_user_invalid_json_keys(self):
        """
        Ensure error is thrown if the JSON object does not have an email key.
        """
        with self.client:
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps({"username": "test"}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Integrity Error:", data["message"])

    def test_register_user_invalid_json_keys(self):
        """
        Ensure error is thrown if the JSON object does not have a email key.
        """
        with self.client:
            response = self.client.post(
                "/users/register",
                data=json.dumps(new_simple_user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Integrity Error:", data["message"])

    def test_subscribe_user_duplicate_email(self):
        """Ensure error is thrown if the email already exists."""
        with self.client:
            self.client.post(
                "/users/subscribe",
                data=json.dumps(new_simple_user_dict),
                content_type="application/json",
            )
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps(new_simple_user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                f'User {new_simple_user_dict["email"]} is already subscribed.',
                data["message"],
            )

    def test_register_user_duplicate_email(self):
        """Ensure error is thrown if the email already exists."""
        with self.client:
            self.client.post(
                "/users/register",
                data=json.dumps(new_user_dict),
                content_type="application/json",
            )
            response = self.client.post(
                "/users/register",
                data=json.dumps(new_user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                f'User {new_user_dict["email"]} already exists.',
                data["message"],
            )


if __name__ == "__main__":
    unittest.main()
