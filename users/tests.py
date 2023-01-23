from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "murodjon",
                "first_name": "Murodjon",
                "last_name": "Abdujabbor",
                "email": "murodjonabdujabbor33@gmail.com",
                "password": "somepassword"
            }
        )

        user = User.objects.get(username="murodjon")

        self.assertEqual(user.first_name, "Murodjon")
        self.assertEqual(user.last_name, "Abdujabbor")
        self.assertEqual(user.email, "murodjonabdujabbor33@gmail.com")
        self.assertNotEqual(user.password, "somepassword")
        self.assertTrue(user.check_password("somepassword"))

    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name": "Murodjon",
                "email": "murodjonabdujabbor33@gmail.com"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "murodjon",
                "first_name": "Murodjon",
                "last_name": "Abdujabbor",
                "email": "invalid-email",
                "password": "somepassword"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_unique_username(self):
        # 1. create a user
        user = User.objects.create(username="murodjon", first_name="Murodjon")
        user.set_password("somepass")
        user.save()

        # 2. try to create another user with that same username
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "murodjon",
                "first_name": "Murodjon",
                "last_name": "Abdujabbor",
                "email": "invalid-email",
                "password": "somepassword"
            }
        )

        # 3. check that the second user was not created
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        # 4. check that the form contains error message
        self.assertFormError(response, "form", "username", "A user with that username already exists.")
