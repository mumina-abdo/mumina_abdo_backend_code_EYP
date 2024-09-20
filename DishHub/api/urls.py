from django.urls import path
from .views import (
    CategoriesView,  
    CategoryDetailView,
    FoodItemsListView,
    FoodItemDetailView,
    IngredientListView,
    IngredientDetailView,  
    PantryListView,
    PantryDetailView,
    RecipeListView,
    FetchRecipeView,
    SearchRecipeView,
)


urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories_list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('food-items/', FoodItemsListView.as_view(), name='food_items_list'),
    path('food-items/<int:id>/', FoodItemDetailView.as_view(), name='food_item_detail'),
    path('categories/<int:category_id>/food-items/', FoodItemsListView.as_view(), name='food_items_in_category'),
    path('categories/<int:category_id>/food-items/<int:id>/', FoodItemDetailView.as_view(), name='food_item_in_category_detail'),
    path('categories/<int:category_id>/food-items/create/', FoodItemDetailView.as_view(), name='food_item_create'),
    path('ingredients/', IngredientListView.as_view(), name="ingredient_list_view"),
    path('ingredients/<int:id>/', IngredientDetailView.as_view(), name='ingredient_detail'),  
    path('pantry/', PantryListView.as_view(), name="pantry_list_view"),
    path('pantry/<int:pk>/', PantryDetailView.as_view(), name='pantry_detail_view'),
    path('pantry/ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient_detail_in_pantry'), 
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:recipe_id>/', FetchRecipeView.as_view(), name='recipe_detail'),
    path('recipes/search/', SearchRecipeView.as_view(), name='recipe_search'),
]

