from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telepon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
