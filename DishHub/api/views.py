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

