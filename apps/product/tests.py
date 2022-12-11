from django.test import TestCase
from .models import Product, Category, Supplier

# Create your tests here.


class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test")
        self.supplier = Supplier.objects.create(
            name="John Doe",
            alamat="JakartaString",
            email="jakartastring@admin.com",
            telepon="082818331312",
            image="url.png",
        )
        self.product = Product.objects.create(
            name="My Product",
            harga="500",
            image="url.png",
            qty=2,
            category=self.category,
            supplier=self.supplier,
        )

    def test_creation_product(self):
        self.assertEqual(self.product.name, "My Product")
        self.assertEqual(self.product.harga, "500")
        self.assertEqual(self.product.qty, 2)
