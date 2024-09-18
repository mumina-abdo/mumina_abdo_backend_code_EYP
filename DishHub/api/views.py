from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import IngredientSerializer, PantrySerializer
from ingredients.models import Ingredients
from pantry.models import Pantry


class IngredientListView(APIView):
    def get(self,request):
        ingredient = Ingredients.objects.all()
        serializer = IngredientSerializer(ingredient,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class IngredientsDetailView(APIView):

    def post(self, request, id):
        ingredients = Ingredients.objects.get(id=id)
        action = request.data.get("action")  

    def get(self, request, id):
        ingredients = Ingredients.objects.get(id=id)
        serializer = IngredientSerializer(Ingredients)
        return Response(serializer.data)    

    def put(self, request, pk):
        ingredients =Ingredients.objects.get(pk = pk)
        serializer = IngredientSerializer(ingredients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)  
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        ingredient = Ingredients.objects.get(pk = pk)
        ingredient.delete()
        return Response(status.HTTP_202_ACCEPTED)


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

    def post(self, request, pk=None):
        pantry = Pantry.objects.get(id=id)
        action = request.data.get("action")
   

    def get(self, request, pk):
        Pantry = Pantry.objects.get(pk=pk)
        serializer = PantrySerializer(Pantry)
        return Response(serializer.data)    

    def put(self, request, pk):
        pantry =Pantry.objects.get(pk=pk)
        serializer = PantrySerializer(pantry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)  
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        pantry = Pantry.objects.get(pk = pk)
        pantry.delete()
        return Response(status.HTTP_202_ACCEPTED)


