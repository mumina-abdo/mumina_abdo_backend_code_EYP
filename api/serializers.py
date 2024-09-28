from rest_framework  import serializers
from django.contrib.auth.hashers import make_password
from users.models import User
from categories.models import Category, FoodItem
from rest_framework.reverse import reverse
from categories.models import Category, FoodItem
from ingredients.models import Ingredients
from pantry.models import Pantry
from shopping.models import ShoppingList, ShoppingListItem
# from .models import User
from django.contrib.auth.hashers import make_password


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ["id",'email', 'password', 'first_name', 'last_name','username', 'registration_date']  
    

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", 'email', 'password', 'first_name', 'last_name', 'username','created_at'] 
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)




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



class ShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = '__all__'

class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingListItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
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





