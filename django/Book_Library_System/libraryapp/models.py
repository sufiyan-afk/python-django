from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    genre = models.CharField(max_length=30)
    price = models.IntegerField()