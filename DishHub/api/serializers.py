from rest_framework import serializers
from ingredients.models import Ingredients
from pantry.models import Pantry

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = '__all__'
