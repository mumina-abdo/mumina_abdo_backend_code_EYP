from django.db import models

class Shoppinglist(models.Model):
    shopping_list_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.shopping_list_id}"


class Shoppinglistitem(models.Model):
    shopping_list_item_id = models.AutoField(primary_key=True)
    shopping_list_id = models.ForeignKey(Shopping_list, on_delete=models.CASCADE, related_name='items') 
    item = models.CharField(max_length=255, default="item")
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100)

    def __str__(self): 
        return f"{self.shopping_list_id} {self.item} {self.quantity} {self.unit}" 
