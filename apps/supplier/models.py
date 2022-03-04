from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=50)
    alamat = models.CharField(max_length=35)
    email = models.EmailField(unique=True)
    telepon = models.CharField(max_length=10)


    def __str__(self):
        return self.name