from django.test import TestCase
from .models import ProductMasuk
from apps.product.models import Product
from apps.supplier.models import Supplier
from apps.category.models import Category

# Create your tests here.
class ProductMasukTestCase(TestCase):
    def setUp(self):
        supplier = Supplier.objects.create(
            name="test", email="test@gmail.com", alamat="test", telepon="test"
        )
        category = Category.objects.create(name="test")
        product = Product.objects.create(
            name="test", harga="1000", qty="10", category=category
        )
        product_masuk = ProductMasuk.objects.create(
            qty="10", tanggal="2020-01-01", product=product, supplier=supplier
        )
        self.supplier = supplier
        self.category = category
        self.product = product
        self.product_masuk = product_masuk

    def test_product_masuk_qty(self):
        self.assertEqual(self.product_masuk.qty, "10")

    def test_product_masuk_tanggal(self):
        self.assertEqual(self.product_masuk.tanggal, "2020-01-01")

    def test_product_masuk_product(self):
        self.assertEqual(self.product_masuk.product, self.product)

    def test_product_masuk_supplier(self):
        self.assertEqual(self.product_masuk.supplier, self.supplier)
