from django.db import models
from django.utils import timezone
from django.db import models


class ShoppingList(models.Model):
    shopping_list_id = models.AutoField(primary_key=True)
    shopping_list_name = models.CharField(max_length=255)  
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.shopping_list_name} (ID: {self.shopping_list_id})"


class ShoppingListItem(models.Model):
    shopping_list_item_id = models.AutoField(primary_key=True)
    shopping_list = models.ForeignKey('ShoppingList', on_delete=models.CASCADE)
    item = models.CharField(max_length=255, default="item")
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100)

    def __str__(self): 
        return f"{self.item} (Quantity: {self.quantity}, Unit: {self.unit})"








