from django.db import models
from apps.utils.models import Timestamp
from apps.product.models import Product
from apps.supplier.models import Supplier

# Create your models here.
class ProductMasuk(Timestamp):
    qty = models.CharField(max_length=5)
    tanggal = models.DateField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
