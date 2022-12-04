from django.db import models

from apps.utils.models import Timestamp
from apps.customer.models import Customer
from apps.product.models import Product

# Create your models here.
class Sale(Timestamp):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(null=False)
    total_price = models.IntegerField(null=False)
    date_transaksi = models.DateField(auto_now=False)

    def __str__(self):
        return self.product.name
