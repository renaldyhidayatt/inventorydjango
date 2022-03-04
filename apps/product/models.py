from django.db import models
from apps.category.models import Category
from apps.utils.models import Timestamp

# Create your models here.
class Product(Timestamp):
    nama = models.CharField(max_length=100)
    harga = models.CharField(max_length=100)
    image = models.ImageField()
    qty = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
