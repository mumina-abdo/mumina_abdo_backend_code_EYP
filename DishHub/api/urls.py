from django.urls import path
from .views import (
    CategoriesListView,
    CategoriesDetailView,
    FoodItemsListView,
    FoodItemsByCategoryView,
    FoodItemsInCategoryDetailView,
)

urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('categories/<int:id>/', CategoriesDetailView.as_view(), name='category_detail'),
    path('food-items/', FoodItemsListView.as_view(), name='food_items_list'),
    path('categories/<int:category_id>/food-items/', FoodItemsByCategoryView.as_view(), name='food_items_by_category'),
    path('categories/<int:category_id>/food-items/<int:food_item_id>/', FoodItemsInCategoryDetailView.as_view(), name='food_item_in_category_detail'),
    path('food-items/search/', FoodItemsListView.as_view(), name='food_items_search'),  # New search endpoint
]
