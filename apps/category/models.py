from django.db import models
from ..utils.models import Timestamp

# Create your models here.
class Category(Timestamp):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
