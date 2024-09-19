from django.urls import path
from .views import (
    CategoriesListView,
    CategoryDetailView,
    FoodItemsListView,
    FoodItemDetailView,
    IngredientListView,
    IngredientsDetailView,
    PantryListView,
    PantryDetailView
)

urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('food-items/', FoodItemsListView.as_view(), name='food-items-list'),
    path('food-items/<int:id>/', FoodItemsListView.as_view(), name='food-item-detail'), 
    path('categories/<int:category_id>/food-items/', FoodItemsListView.as_view(), name='food-items-in-category'),
    path('categories/<int:category_id>/food-items/<int:id>/', FoodItemsListView.as_view(), name='food-item-in-category-detail'),
    path('categories/<int:category_id>/food-items/create/', FoodItemDetailView.as_view(), name='food-item-create'),
    path('ingredients/', IngredientListView.as_view(), name="ingredient_list_view"),
    path('ingredients/<int:id>/', IngredientsDetailView.as_view(), name='ingredient-detail'),
    path('pantry/', PantryListView.as_view(), name="pantry_list_view"),
    path('pantry/<int:pk>/', PantryDetailView.as_view(), name='pantry-detail_view'),
    path('pantry/ingredients/<int:pk>/', IngredientsDetailView.as_view(), name='ingredient-detail'),
]
