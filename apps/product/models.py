from django.db import models
from apps.category.models import Category

# Create your models here.
class Product(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.CharField(max_length=100)
    image = models.ImageField()
    qty = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
