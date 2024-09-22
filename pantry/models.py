from django.db import models
from ingredients.models import Ingredients
from users.models import User


class Pantry(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.CharField(max_length = 20)
    item = models.CharField(max_length = 20)
    ingredient = models.ManyToManyField(Ingredients)
    # users = models.CharField(max_length = 20)
    user = models.ManyToManyField(User)


    def __str__(self):
        return f"{self.quantity} {self.item}"

# Create your models here.