from datetime import timezone
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from .serializers import UserSerializer
import json
import logging
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .serializers import CategoriesSerializer, FoodItemsSerializer
from django.shortcuts import get_object_or_404
from categories.models import Category, FoodItem
from api.serializers import IngredientSerializer, PantrySerializer
from ingredients.models import Ingredients
from pantry.models import Pantry
from django.http import JsonResponse
from django.shortcuts import render
from api.serializers import IngredientSerializer, PantrySerializer
from ingredients.models import Ingredients
from pantry.models import Pantry
from rest_framework.exceptions import NotFound, ValidationError
from shopping.models import ShoppingList, ShoppingListItem
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer



User= get_user_model()
logger = logging.getLogger(__name__)




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








class ShoppingListList(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ValidationError as ve:
            return Response({"error": ve.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)








class ShoppingListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except NotFound:
            return Response({"error": "Shopping list not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except ValidationError as ve:
            return Response({"error": ve.detail}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound:
            return Response({"error": "Shopping list not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            shopping_list = self.get_object()  
            self.perform_destroy(shopping_list)  
            return Response(
                {"message": "Shopping list deleted successfully.", "deleted_item": self.serializer_class(shopping_list).data},
                status=status.HTTP_200_OK 
            )
        except NotFound:
            return Response({"error": "Shopping list not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)








class ShoppingListItemList(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListItemSerializer

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ValidationError as ve:
            return Response({"error": ve.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class ShoppingListItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except NotFound:
            return Response({"error": "Shopping list item not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except ValidationError as ve:
            return Response({"error": ve.detail}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound:
            return Response({"error": "Shopping list item not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            shopping_list_item = self.get_object()  
            self.perform_destroy(shopping_list_item)  
            return Response(
                {"message": "Shopping list item deleted successfully.", "deleted_item": self.serializer_class(shopping_list_item).data},
                status=status.HTTP_200_OK  
            )
        except NotFound:
            return Response({"error": "Shopping list item not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)            





class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
          
            logger.info(f'User registered successfully: {user.email}')
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        
        logger.error(f'User registration failed: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        logger.info('Fetched user details successfully.')
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('username')
        password = request.data.get('password')
        print(f"$$$${email}$$$$$$$$$$$$$$$$$$$$$$$$$$$$${password}$$$$$$$$$")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            print("*********************************")
            refresh = RefreshToken.for_user(user)
            return Response({
                 "Login successful! Welcome back!",
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



class UserProfileUpdateView(APIView):
    def get_object(self, pk):
        return User.objects.get(pk=pk)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        logger.info(f'User profile retrieved successfully: {user.email}')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User profile updated successfully: {user.email}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'User profile update failed: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        model = self.get_object(pk)
        serializer = UserSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User profile updated successfully: {user.email}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'User profile update failed for {request.user.email}: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
def generate_token(request):
    user,created =User.objects.get_or_create(username=' ')
    refresh = RefreshToken.for_user(user)
    return JsonResponse({
        'access':str(refresh.access_token),
        'refresh':str(refresh)
})




class CategoriesView(APIView):
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
    def get(self, request, category_id=None):
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

    def put(self, request, id):
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

class IngredientDetailView(APIView):
    def get(self, request, id):
        ingredient = get_object_or_404(Ingredients, id=id)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def put(self, request, id):
        ingredient = get_object_or_404(Ingredients, id=id)
        serializer = IngredientSerializer(instance=ingredient, data=request.data)
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
        serializer = PantrySerializer(instance=pantry_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pantry_item = get_object_or_404(Pantry, pk=pk)
        pantry_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecipeListView(APIView):
    def get(self, request):
        ingredients = request.GET.get('ingredients')
        if not ingredients:
            return JsonResponse({'error': 'Ingredients parameter is required.'}, status=400)

        url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredients}"
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch recipes from MealDB.'}, status=response.status_code)

class FetchRecipeView(APIView):
    def get(self, request, recipe_id):
        url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={recipe_id}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch the recipe from MealDB.'}, status=response.status_code)

class SearchRecipeView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        if not query:
            return JsonResponse({'error': 'Query parameter "q" is required.'}, status=400)

        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch the recipe from MealDB.'}, status=response.status_code)
 


