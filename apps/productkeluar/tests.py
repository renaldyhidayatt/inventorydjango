from django.test import TestCase
from .models import ProductKeluar
from apps.product.models import Product
from apps.customer.models import Customer
from apps.category.models import Category

# Create your tests here.
class ProductKeluarTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(
            name="test", email="test@gmail.com", alamat="test", telepon="test"
        )
        category = Category.objects.create(name="test")

        product = Product.objects.create(
            name="test", harga="1000", qty="test", category=category
        )
        product_keluar = ProductKeluar.objects.create(
            qty="test", tanggal="2020-01-01", product=product, customer=customer
        )

        self.customer = customer
        self.product = product
        self.product_keluar = product_keluar

    def test_product_keluar_qty(self):
        self.assertEqual(self.product_keluar.qty, "test")

    def test_product_keluar_tanggal(self):
        self.assertEqual(self.product_keluar.tanggal, "2020-01-01")

    def test_product_keluar_product(self):
        self.assertEqual(self.product_keluar.product, self.product)

    def test_product_keluar_customer(self):
        self.assertEqual(self.product_keluar.customer, self.customer)
