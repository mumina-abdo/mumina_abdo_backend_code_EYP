from rest_framework import serializers
from ingredients.models import Ingredients
from pantry.models import Pantry
from shopping.models import Shopping_list, Shopping_list_item


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = '__all__'



class ShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping_list_item
        fields = '__all__'

class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingListItemSerializer(many=True, read_only=True)

    class Meta:
        model = Shopping_list
        fields = '__all__'