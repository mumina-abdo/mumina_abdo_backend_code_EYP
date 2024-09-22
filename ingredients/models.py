# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from categories.models import Category

class Ingredients(models.Model):
    ingredients_id = models.AutoField(primary_key=True)
    ingredients_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    # category = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category)


    def clean(self):
        if self.quantity is None:
            raise ValidationError('Quantity cannot be None.')
        if self.quantity < 0:
            raise ValidationError('Quantity cannot be negative.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ingredients_id} {self.ingredients_name}"

