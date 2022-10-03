from django.db import models
from products.models import Product

# Create your models here.
class Purchase(models.Model):
  products = models.ManyToManyField(Product)
  total = models.FloatField()
