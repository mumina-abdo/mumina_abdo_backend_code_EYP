<<<<<<< HEAD
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from categories.models import Category, FoodItem
from .serializers import CategoriesSerializer, FoodItemsSerializer

class CategoriesListView(APIView):
    def get(self, request):
        try:
            categories_list = Category.objects.all()
            serializer = CategoriesSerializer(categories_list, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    def get(self, request, id):
        category_instance = get_object_or_404(Category, id=id)
        serializer = CategoriesSerializer(category_instance)
        return Response(serializer.data)

    def put(self, request, id):
        category_instance = get_object_or_404(Category, id=id)
        serializer = CategoriesSerializer(instance=category_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodItemsListView(APIView):


    def post(self, request, category_id=None):
        category_instance = get_object_or_404(Category, id=category_id)
        serializer = FoodItemsSerializer(data=request.data)
        if serializer.is_valid():
            food_item = serializer.save(category=category_instance)
            return Response(FoodItemsSerializer(food_item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None, category_id=None):
        if id is not None:
            food_item = get_object_or_404(FoodItem, id=id)
            serializer = FoodItemsSerializer(food_item)
            return Response(serializer.data)

        food_items = FoodItem.objects.all()
        if category_id:
            food_items = food_items.filter(category__id=category_id)

        serializer = FoodItemsSerializer(food_items, many=True)
        return Response(serializer.data)

   

class FoodItemDetailView(APIView):
    

    def get(self, request, id=None):
        if id is not None:
            food_item = get_object_or_404(FoodItem, id=id)
            serializer = FoodItemsSerializer(food_item)
            return Response(serializer.data)

        food_items = FoodItem.objects.all()
        serializer = FoodItemsSerializer(food_items, many=True)
        return Response(serializer.data)
    

    def put(self, request, id=None, category_id=None):
        if category_id:
            category_instance = get_object_or_404(Category, id=category_id)
            food_item = get_object_or_404(FoodItem, id=id, category=category_instance)
        else:
            food_item = get_object_or_404(FoodItem, id=id)

        serializer = FoodItemsSerializer(instance=food_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import IngredientSerializer, PantrySerializer
from ingredients.models import Ingredients
from pantry.models import Pantry


class IngredientListView(APIView):
    def get(self, request):
        ingredients = Ingredients.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientsDetailView(APIView):
    
    def get(self, request, id):
        try:
            ingredient = Ingredients.objects.get(id=id)
            serializer = IngredientSerializer(ingredient)
            return Response(serializer.data)
        except Ingredients.DoesNotExist:
            return Response({"error": "Ingredient not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            ingredient = Ingredients.objects.get(pk=pk)
            serializer = IngredientSerializer(ingredient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Ingredients.DoesNotExist:
            return Response({"error": "Ingredient not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            ingredient = Ingredients.objects.get(pk=pk)
            ingredient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Ingredients.DoesNotExist:
            return Response({"error": "Ingredient not found."}, status=status.HTTP_404_NOT_FOUND)


class PantryListView(APIView):
    def get(self, request):
        item = request.GET.get('item', None)
        pantry = Pantry.objects.all()

        if item:
            pantry = pantry.filter(item=item)

        serializer = PantrySerializer(pantry, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PantrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PantryDetailView(APIView):

    def get(self, request, pk):
        try:
            pantry_item = Pantry.objects.get(pk=pk)
            serializer = PantrySerializer(pantry_item)
            return Response(serializer.data)
        except Pantry.DoesNotExist:
            return Response({"error": "Pantry item not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            pantry_item = Pantry.objects.get(pk=pk)
            serializer = PantrySerializer(pantry_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pantry.DoesNotExist:
            return Response({"error": "Pantry item not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            pantry_item = Pantry.objects.get(pk=pk)
            pantry_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Pantry.DoesNotExist:
            return Response({"error": "Pantry item not found."}, status=status.HTTP_404_NOT_FOUND)

