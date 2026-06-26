from django.db import models
# Create your models here.

class Stock(models.Model):
    name = models.CharField(max_length=70)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()
    material = models.CharField(max_length=50)
    