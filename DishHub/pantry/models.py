from django.db import models
from ingredients.models import Ingredients


class User(models.Model):
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pantry(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.CharField(max_length = 20)
    item = models.CharField(max_length = 20)
    ingredient = models.ManyToManyField(Ingredients)
    users = models.ManyToManyField(User, blank=True)


    def __str__(self):
        return f"{self.quantity} {self.item}"

# Create your models here.