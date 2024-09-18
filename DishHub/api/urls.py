from django.urls import path
from .views import RegisterView, LoginView, UserProfileUpdateView, UserListView, UserDetailView
# from . import views
from .views import generate_token
from .views import UserProfileUpdateView


urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/register/', RegisterView.as_view(), name='user-register'),
    path('users/login/', LoginView.as_view(), name='user-login'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/profile/update/', UserProfileUpdateView.as_view(), name='user-profile-update'),
    path('generate_token/', generate_token, name='generate_token'),  

]

from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    UserProfileUpdateView,
    UserListView,
    UserDetailView,
    generate_token,
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/register/', RegisterView.as_view(), name='user-register'),
    path('users/login/', LoginView.as_view(), name='user-login'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/profile/update/', UserProfileUpdateView.as_view(), name='user-profile-update'),
    path('generate_token/', generate_token, name='generate_token'),  
]


