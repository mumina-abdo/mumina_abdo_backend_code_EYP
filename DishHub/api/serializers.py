from rest_framework import serializers
from categories.models import Category, FoodItem


class FoodItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'quantity', 'category']

class CategoriesSerializer(serializers.ModelSerializer):
    food_items = FoodItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'updated_at', 'food_items']





