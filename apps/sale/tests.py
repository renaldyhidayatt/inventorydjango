from django.test import TestCase
from django.utils import timezone
from .models import Sale
from apps.product.models import Product
from apps.customer.models import Customer
from apps.category.models import Category
from apps.supplier.models import Supplier

# Create your tests here.
class SaleTestCase(TestCase):
    def setUp(self):
        # Buat objek Customer dan Product untuk menguji Sale
        self.customer = Customer.objects.create(
            name="John Doe",
            alamat="JakartaString",
            email="jakartastring@admin.com",
            telepon="082818331312",
        )

        self.category = Category.objects.create(name="bumbu")
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
            category=self.category,
            supplier=self.supplier,
        )

    def test_sale_creation(self):
        # Buat objek Sale
        qty = 2
        harga = qty * int(self.product.harga)

        sale = Sale.objects.create(
            customer=self.customer,
            product=self.product,
            qty=qty,
            total_price=harga,
            date_transaksi=timezone.now(),
        )

        # Pastikan Sale yang dibuat sesuai dengan yang diharapkan
        self.assertEqual(sale.product.name, "My Product")
        self.assertEqual(sale.qty, 2)
        self.assertEqual(sale.total_price, 1000)
