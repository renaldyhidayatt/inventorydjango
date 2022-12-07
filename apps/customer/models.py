from django.db import models
from apps.utils.models import Timestamp

# Create your models here.
class Customer(Timestamp):
    name = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telepon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
