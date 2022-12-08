from django.db import models
from datetime import datetime


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    preparation = models.TextField()
    preparation_time = models.IntegerField()
    serving = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_recipe = models.DateTimeField(default=datetime.now, blank=True)
