from django.test import TestCase
from .models import Product
from .models import Category

# Create your tests here.


class ProductTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.create(name="test")
        prod = Product.objects.create(
            name="test", harga="1000", qty="test", category=cat
        )
        self.cat = cat
        self.prod = prod

    def test_product_name(self):
        self.assertEqual(self.prod.name, "test")

    def test_product_harga(self):
        self.assertEqual(self.prod.harga, "1000")

    def test_product_qty(self):
        self.assertEqual(self.prod.qty, "test")

    def test_product_category(self):
        self.assertEqual(self.prod.category, self.cat)
