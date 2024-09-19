from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from categories.models import Category, FoodItem
from api.serializers import IngredientSerializer, PantrySerializer
from .serializers import CategoriesSerializer, FoodItemsSerializer
from ingredients.models import Ingredients
from pantry.models import Pantry

class CategoriesListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategoriesSerializer(category)
        return Response(serializer.data)

    def put(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategoriesSerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodItemsListView(APIView):
    def get(self, request, id=None, category_id=None):
        if id:
            food_item = get_object_or_404(FoodItem, id=id)
            serializer = FoodItemsSerializer(food_item)
            return Response(serializer.data)

        food_items = FoodItem.objects.all()
        if category_id:
            food_items = food_items.filter(category__id=category_id)

        serializer = FoodItemsSerializer(food_items, many=True)
        return Response(serializer.data)

    def post(self, request, category_id=None):
        category = get_object_or_404(Category, id=category_id)
        serializer = FoodItemsSerializer(data=request.data)
        if serializer.is_valid():
            food_item = serializer.save(category=category)
            return Response(FoodItemsSerializer(food_item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodItemDetailView(APIView):
    def get(self, request, id):
        food_item = get_object_or_404(FoodItem, id=id)
        serializer = FoodItemsSerializer(food_item)
        return Response(serializer.data)

    def put(self, request, id, category_id=None):
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            food_item = get_object_or_404(FoodItem, id=id, category=category)
        else:
            food_item = get_object_or_404(FoodItem, id=id)

        serializer = FoodItemsSerializer(instance=food_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientsDetailView(APIView):
    def get(self, request, id):
        ingredient = get_object_or_404(Ingredients, id=id)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def put(self, request, id):
        ingredient = get_object_or_404(Ingredients, id=id)
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        ingredient = get_object_or_404(Ingredients, id=id)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PantryListView(APIView):
    def get(self, request):
        item = request.GET.get('item', None)
        pantry = Pantry.objects.all()
        if item:
            pantry = pantry.filter(item=item)
        serializer = PantrySerializer(pantry, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PantrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PantryDetailView(APIView):
    def get(self, request, pk):
        pantry_item = get_object_or_404(Pantry, pk=pk)
        serializer = PantrySerializer(pantry_item)
        return Response(serializer.data)

    def put(self, request, pk):
        pantry_item = get_object_or_404(Pantry, pk=pk)
        serializer = PantrySerializer(pantry_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pantry_item = get_object_or_404(Pantry, pk=pk)
        pantry_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
