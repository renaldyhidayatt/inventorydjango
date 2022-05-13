from django.test import TestCase
from .models import Sale

# Create your tests here.
class SaleTestCase(TestCase):
    def setUp(self):
        sale = Sale.objects.create(
            name="test", alamat="test", telepon="08889292221", email="test@gmail.com"
        )

        self.sale = sale

    def test_sale_name(self):
        self.assertEqual(self.sale.name, "test")

    def test_sale_alamat(self):
        self.assertEqual(self.sale.alamat, "test")

    def test_sale_telepon(self):
        self.assertEqual(self.sale.telepon, "08889292221")

    def test_sale_email(self):
        self.assertEqual(self.sale.email, "test@gmail.com")
