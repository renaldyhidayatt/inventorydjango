from django.db import models
from apps.category.models import Category
from apps.supplier.models import Supplier
from apps.utils.models import Timestamp

# Create your models here.
class Product(Timestamp):
    name = models.CharField(max_length=100, null=False)
    harga = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to="products/image", default="image/default.png")
    qty = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
