from rest_framework import serializers
from rest_framework.reverse import reverse
from categories.models import Category, FoodItem
from ingredients.models import Ingredients
from pantry.models import Pantry

class FoodItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'quantity', 'category']

class CategoriesSerializer(serializers.ModelSerializer):
    food_items = FoodItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'updated_at', 'food_items']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = '__all__'

class MealSerializer(serializers.Serializer):
    idMeal = serializers.CharField()
    strMeal = serializers.CharField()
    strDrinkAlternate = serializers.CharField(allow_blank=True)
    strCategory = serializers.CharField()
    strArea = serializers.CharField()
    strInstructions = serializers.CharField()
    strMealThumb = serializers.CharField()  
    strTags = serializers.CharField(allow_blank=True)
    strYoutube = serializers.CharField(allow_blank=True)
