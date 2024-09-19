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