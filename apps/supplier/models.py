from django.db import models

from apps.utils.models import Timestamp

# Create your models here.
class Supplier(Timestamp):
    name = models.CharField(max_length=50)
    alamat = models.CharField(max_length=35)
    email = models.EmailField(unique=False, max_length=20)
    telepon = models.CharField(max_length=10)
    image = models.ImageField(upload_to="supplier/image", default="image/default.png")

    def __str__(self) -> str:
        return self.name
