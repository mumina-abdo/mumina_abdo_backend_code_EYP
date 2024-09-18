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

class CategoriesDetailView(APIView):
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
    def get(self, request):
        name = request.GET.get('name', None)
        food_items = FoodItem.objects.all()

        if name:
            food_items = food_items.filter(name__icontains=name)
        serializer = FoodItemsSerializer(food_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodItemsByCategoryView(APIView):
    def get(self, request, category_id):
        category_instance = get_object_or_404(Category, id=category_id)
        food_items = category_instance.food_items.all()
        name = request.GET.get('name', None) 
        if name:
            food_items = food_items.filter(name__icontains=name)

        serializer = FoodItemsSerializer(food_items, many=True)
        return Response(serializer.data)

    def post(self, request, category_id):
        category_instance = get_object_or_404(Category, id=category_id)
        serializer = FoodItemsSerializer(data=request.data)
        if serializer.is_valid():
            food_item = serializer.save(category=category_instance)
            return Response(FoodItemsSerializer(food_item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodItemsDetailView(APIView):
    def get(self, request, id):
        food_item = get_object_or_404(FoodItem, id=id)
        serializer = FoodItemsSerializer(food_item)
        return Response(serializer.data)

    def put(self, request, id):
        food_item = get_object_or_404(FoodItem, id=id)
        serializer = FoodItemsSerializer(instance=food_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        food_item = get_object_or_404(FoodItem, id=id)
        food_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FoodItemsInCategoryDetailView(APIView):
    def get(self, request, category_id, food_item_id):
        category_instance = get_object_or_404(Category, id=category_id)
        food_item = get_object_or_404(FoodItem, id=food_item_id, category=category_instance)
        serializer = FoodItemsSerializer(food_item)
        return Response(serializer.data)

    def put(self, request, category_id, food_item_id):
        category_instance = get_object_or_404(Category, id=category_id)
        food_item = get_object_or_404(FoodItem, id=food_item_id, category=category_instance)
        serializer = FoodItemsSerializer(instance=food_item, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id, food_item_id):
        category_instance = get_object_or_404(Category, id=category_id)
        food_item = get_object_or_404(FoodItem, id=food_item_id, category=category_instance)
        food_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
