from django.urls import path
from .views import (
    ShoppingListList,
    ShoppingListDetail,
    ShoppingListItemList,
    ShoppingListItemDetail,
)

urlpatterns = [
    path('shopping-lists/', ShoppingListList.as_view(), name='shopping-list-list'),
    path('shopping-lists/<int:pk>/', ShoppingListDetail.as_view(), name='shopping-list-detail'),
    path('shopping-list-items/', ShoppingListItemList.as_view(), name='shopping-list-item-list'),
    path('shopping-list-items/<int:pk>/', ShoppingListItemDetail.as_view(), name='shopping-list-item-detail'),
]