from django.db import models

# Create your models here.

class Players(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    age = models.IntegerField()
    state = models.CharField(max_length=20)