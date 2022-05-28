from django.db import models
from apps.utils.models import Timestamp
from apps.product.models import Product
from apps.customer.models import Customer

# Create your models here.
class ProductKeluar(Timestamp):
    qty = models.CharField(max_length=5)
    tanggal = models.DateField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
