from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField()
  stock = models.IntegerField()
  stock_orders = models.ManyToManyField('StockOrder', through='StockOrderForProduct')

  def __str__(self):
    return self.name

class StockOrder(models.Model):
  products = models.ManyToManyField(Product, through='StockOrderForProduct')
  

class StockOrderForProduct(models.Model):
  stock_order = models.ForeignKey(StockOrder)
  product = models.ForeignKey(Product)

  def __str__(self):
    return "{}_{}".format(self.stock_order.__str__(), self.product.__str__())

