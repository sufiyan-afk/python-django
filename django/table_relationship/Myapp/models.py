from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
    
class Passport(models.Model):
    person = models.OneToOneField(Person , on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    pid = models.CharField(max_length=20)
    
    def __str__(self):
        return self.pid
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
    
class Book(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
    
class Author(models.Model):
    book = models.ManyToManyField(Book)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    