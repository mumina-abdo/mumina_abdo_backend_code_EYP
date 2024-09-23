from django.contrib import admin
from shopping.models import ShoppingList, ShoppingListItem 


# Register your models here.
admin.site.register(ShoppingList)
admin.site.register(ShoppingListItem)

