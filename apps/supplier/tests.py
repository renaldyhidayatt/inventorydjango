from django.test import TestCase
from .models import Supplier


# Create your tests here.
class SupplierTestCase(TestCase):
    def setUp(self):
        supplier = Supplier.objects.create(
            name="test", alamat="test", telepon="08812182191", email="test@gmail.com"
        )
        self.supplier = supplier

    def test_supplier_name(self):
        self.assertEqual(self.supplier.name, "test")

    def test_supplier_alamat(self):
        self.assertEqual(self.supplier.alamat, "test")

    def test_supplier_telepon(self):
        self.assertEqual(self.supplier.telepon, "08812182191")

    def test_supplier_email(self):
        self.assertEqual(self.supplier.email, "test@gmail.com")
