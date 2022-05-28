from django.db import models

from apps.utils.models import Timestamp

# Create your models here.
class Sale(Timestamp):
    name = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telepon = models.CharField(max_length=13)

    def __str__(self):
        return self.name
