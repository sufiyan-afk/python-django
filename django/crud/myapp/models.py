from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    age = models.IntegerField()

# class team(models.Model):
#     name = models.CharField(max_length=20)
#     no_of_players = models.IntegerField()
#     email = models.CharField(max_length=20)