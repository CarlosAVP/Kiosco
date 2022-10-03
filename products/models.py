from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField()
  stock = models.IntegerField()
  barcode = models.CharField(max_length=13)

  def __str__(self):
    return self.name

class StockOrder(models.Model):
  products = models.ManyToManyField(Product, through='StockOrderForProduct')

class StockOrderForProduct(models.Model):
  stock_order = models.ForeignKey(StockOrder, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()
