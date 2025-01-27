from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    categories_table = [
        ("Breakfast",'Breakfast'),
        ("Lunch",'Lunch'),
        ("Dinner",'Dinner'),
    ]
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instruction = models.TextField()
    catrgory = models.CharField(max_length=30,choices=categories_table)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title