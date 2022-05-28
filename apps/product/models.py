from django.db import models
from apps.category.models import Category
from apps.utils.models import Timestamp

# Create your models here.
class Product(Timestamp):
    name = models.CharField(max_length=100)
    harga = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/image", default="image/default.png")
    qty = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
