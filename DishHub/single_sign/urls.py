from django.urls import path
from . import views
from .views import generate_token


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),
    path('logout/', views.logout, name='logout'),
    path('generate-token/', generate_token, name='generate_token'),

]
