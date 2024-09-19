from django.urls import path
from .views import (
    CategoriesListView,
    CategoryDetailView,
    FoodItemsListView,
    FoodItemDetailView,  
)

urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('food-items/', FoodItemsListView.as_view(), name='food-items-list'),
    path('food-items/<int:id>/', FoodItemsListView.as_view(), name='food-item-detail'), 
    path('categories/<int:category_id>/food-items/', FoodItemsListView.as_view(), name='food-items-in-category'),
    path('categories/<int:category_id>/food-items/<int:id>/', FoodItemsListView.as_view(), name='food-item-in-category-detail'),
    path('categories/<int:category_id>/food-items/create/', FoodItemDetailView.as_view(), name='food-item-create'),  
]
