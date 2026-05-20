from django.db import models

# Create your models here.
class Netflix(models.Model):
    movie_name = models.CharField(max_length=20)
    hero_name = models.CharField(max_length=20)
    rating = models.IntegerField()
    review = models.CharField