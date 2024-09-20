from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("callback", views.callback, name="callback"),
    path('auth/', index, name='index'),
    path("logout/", views.logout, name='logout'),

]



