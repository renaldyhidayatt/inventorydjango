from django.test import TestCase
from .models import Customer

# Create your tests here.
class CustomerTestCase(TestCase):
    def setUp(self):
        cat = Customer.objects.create(
            name="test", email="test@gmail.com", alamat="test", telepon="test"
        )
        self.cat = cat

    def test_customer_name(self):
        self.assertEqual(self.cat.name, "test")

    def test_customer_email(self):
        self.assertEqual(self.cat.email, "test@gmail.com")

    def test_customer_alamat(self):
        self.assertEqual(self.cat.alamat, "test")
