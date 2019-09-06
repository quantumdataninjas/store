from copy import deepcopy
import json
import unittest
from project import db
from project.api.models import (
    SimpleUser,
    User,
    Address,
)
from project.tests.base import BaseTestCase
from project.utils import (
    simple_user_dict,
    simple_user_dict2,
    user_dict,
    user_dict2,
    add_simple_user,
    add_user,
)


# def add_simple_user(new_simple_user):
#     simple_user = simpleuser(**new_simple_user)
#     db.session.add(simple_user)
#     db.session.commit()
#     return simple_user


# def add_user(new_user):
#     simple_user = simpleuser.query.filter_by(email=new_user["email"]).first()
#     if not simple_user:
#         simple_user = add_simple_user({"email": new_user["email"]})
#     # new_user["simple_user_id"] = simple_user.id
#     addresses = new_user["addresses"]
#     del new_user["addresses"]
#     user = user(**new_user, simple_user_id=simple_user.id)
#     db.session.add(user)
#     for i, address in enumerate(addresses):
#         addresses[i] = address(**address, user_id=user.id)
#         db.session.add(addresses[i])
#     user.addresses = addresses
#     db.session.commit()
#     return user


class TestUsersService(BaseTestCase):
    """
    Tests for the Users Service.
    """

    def test_get_users_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get("/users/ping")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("pong!", data["message"])

    def test_get_all_simple_users(self):
        """
        Ensure get all simple users behaves correctly.
        """
        add_simple_user(simple_user_dict)
        add_simple_user(simple_user_dict2)
        with self.client:
            response = self.client.get("/users/simple")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data["simple_users"]), 2)
            self.assertIn(
                "user@test.org", data["simple_users"][0]["email"]
            )
            self.assertIn(
                "user2@test.org", data["simple_users"][1]["email"]
            )

    def test_get_simple_user(self):
        """
        Ensure get single user behaves correctly.
        """
        simple_user = add_simple_user(simple_user_dict)
        with self.client:
            response = self.client.get(f"/users/simple/{simple_user.id}")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                simple_user.email,
                data["simple_user"]["email"]
            )

    def test_get_simple_user_with_string(self):
        """
        Ensure error is thrown if an id is not provided.
        """
        with self.client:
            response = self.client.get("/users/simple/blah")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("Value Error:", data["message"])

    def test_get_simple_user_incorrect_id(self):
        """
        Ensure error is thrown if the id does not exist.
        """
        with self.client:
            response = self.client.get("/users/simple/999")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("User does not exist.", data["message"])

    def test_subscribe(self):
        """
        Ensure a new user can subscribe for emails.
        """
        with self.client:
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps(simple_user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            simple_user = SimpleUser.query.filter_by(
                email=simple_user_dict["email"]
            ).first()
            self.assertEqual(
                simple_user.email,
                simple_user_dict["email"]
            )
            self.assertIn(
                f"{simple_user.email} is subscribed!", data["message"]
            )

    def test_subscribe_with_str(self):
        """
        Ensure error is thrown if the post data is not a JSON object.
        """
        with self.client:
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps("not json"),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                "Type Error: Post data must be JSON.",
                data["message"]
            )

    def test_subscribe_with_empty_json(self):
        """
        Ensure error is thrown if the JSON object is empty.
        """
        with self.client:
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps({}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])

    def test_subscribe_with_invalid_json(self):
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
            self.assertIn("Key Error:", data["message"])

    def test_subscribe_with_invalid_email(self):
        """
        Ensure error is thrown if the email is invalid.
        """
        with self.client:
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps({**simple_user_dict, "email": "invalid"}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn("invalid is not a valid email.", data["message"])

    def test_subscribe_with_duplicate_email(self):
        """
        Ensure error is thrown if the email already exists.
        """
        with self.client:
            self.client.post(
                "/users/subscribe",
                data=json.dumps(simple_user_dict),
                content_type="application/json",
            )
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps(simple_user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            # TODO: test if this works
            self.assertIn(
                f'{simple_user_dict["email"]} is already subscribed.',
                data["message"],
            )

    def test_unsubscribe(self):
        """
        Ensure a new user can subscribe for emails.
        """
        with self.client:
            response = self.client.post(
                "/users/subscribe",
                data=json.dumps(simple_user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            simple_user = SimpleUser.query.filter_by(
                email=simple_user_dict["email"]
            ).first()
            self.assertEqual(
                simple_user.email,
                simple_user_dict["email"]
            )
            self.assertIn(
                f"{simple_user.email} is subscribed!", data["message"]
            )

    def test_get_all_users(self):
        """
        Ensure get all users behaves correctly.
        """
        add_user(deepcopy(user_dict))
        add_user(deepcopy(user_dict2))
        with self.client:
            response = self.client.get("/users")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data["users"]), 2)
            self.assertIn("user@test.org", data["users"][0]["email"])
            self.assertIn("user2@test.org", data["users"][1]["email"])

    def test_get_user(self):
        """
        Ensure get single user behaves correctly.
        """
        user = add_user(deepcopy(user_dict))
        with self.client:
            response = self.client.get(f"/users/{user.id}")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn(user.email, data["user"]["email"])

    def test_get_user_with_string(self):
        """
        Ensure error is thrown if an id is not provided.
        """
        with self.client:
            response = self.client.get("/users/blah")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("Value Error:", data["message"])

    def test_get_user_incorrect_id(self):
        """
        Ensure error is thrown if the id does not exist.
        """
        with self.client:
            response = self.client.get("/users/999")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("User does not exist.", data["message"])

    def test_user_can_signup(self):
        """
        Ensure a new user can signup.
        """
        with self.client:
            response = self.client.post(
                "/users/signup",
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
                "/users/signup",
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
                "/users/signup",
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
                "/users/signup",
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
                "/users/signup",
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
                "/users/signup",
                data=json.dumps(user_dict),
                content_type="application/json",
            )
            response = self.client.post(
                "/users/signup",
                data=json.dumps(user_dict),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                f'User {user_dict["email"]} already exists.',
                data["message"],
            )


if __name__ == "__main__":
    unittest.main()
