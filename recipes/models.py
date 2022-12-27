from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


from django.db.models import BooleanField

from persons.models import Person


class Recipe(models.Model):
    # person = models.ForeignKey(Person, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    preparation = models.TextField()
    preparation_time = models.IntegerField()
    serving = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_recipe = models.DateTimeField(default=datetime.now, blank=True)
    publicated = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return f"{self.name} serving {self.serving} since {self.date_recipe} ({self.category})"
