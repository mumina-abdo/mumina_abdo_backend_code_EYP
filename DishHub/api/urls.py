from django.urls import path
from .views import RegisterView, LoginView, UserProfileUpdateView, UserListView, UserDetailView
from . import views
from .views import generate_token
from .views import UserProfileUpdateView
from single_sign.views import *


urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/register/', RegisterView.as_view(), name='user-register'),
    path('users/login/', LoginView.as_view(), name='user-login'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/profile/update/<int:pk>/', UserProfileUpdateView.as_view(), name='user-profile-update'),
    # path('', views.index, name='index'),
    path('login/', login, name='login'),
    path('callback/', callback, name='callback'),
    path('generate-token/', views.generate_token, name='generate_token'),

]