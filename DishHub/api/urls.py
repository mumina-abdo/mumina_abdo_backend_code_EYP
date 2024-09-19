from django.urls import path, include
from .views import (
    IngredientListView,
    IngredientsDetailView,
    PantryListView,
    PantryDetailView,

    ShoppingListList,
    ShoppingListDetail,
    ShoppingListItemList,
    ShoppingListItemDetail,
)

urlpatterns = [
    path('ingredients/', IngredientListView.as_view(), name="ingredient_list_view"),
    path('ingredients/<int:id>/', IngredientsDetailView.as_view(), name='ingredient-detail'),
    path('pantry/', PantryListView.as_view(), name="pantry_list_view"),
    path("pantry/<int:pk>/", PantryDetailView.as_view(), name='pantry-detail_view'),
    path('pantry/ingredients/<int:pk>/', IngredientsDetailView.as_view(), name='ingredient-detail'), 

    path('shopping-lists/', ShoppingListList.as_view(), name='shopping-list-list'),
    path('shopping-lists/<int:pk>/', ShoppingListDetail.as_view(), name='shopping-list-detail'),
    path('shopping-list-items/', ShoppingListItemList.as_view(), name='shopping-list-item-list'),
    path('shopping-list-items/<int:pk>/', ShoppingListItemDetail.as_view(), name='shopping-list-item-detail'),
]
   


