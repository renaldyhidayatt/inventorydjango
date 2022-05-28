from django.test import TestCase
from .models import Users

# Create your tests here.


class UsersTestCase(TestCase):
    def setUp(self):
        user = Users.objects.create(
            first_name="test",
            last_name="test",
            email="test@gmail.com",
            phone_number="088822992",
            is_admin=True,
            is_staff=True,
            is_superuser=True,
        )
        self.user = user

    def test_user_first_name(self):
        self.assertEqual(self.user.first_name, "test")

    def test_user_last_name(self):
        self.assertEqual(self.user.last_name, "test")

    def test_user_email(self):
        self.assertEqual(self.user.email, "test@gmail.com")

    def test_user_phone_number(self):
        self.assertEqual(self.user.phone_number, "088822992")

    def test_user_is_admin(self):
        self.assertEqual(self.user.is_admin, True)

    def test_user_is_staff(self):
        self.assertEqual(self.user.is_staff, True)

    def test_user_is_superuser(self):
        self.assertEqual(self.user.is_superuser, True)
