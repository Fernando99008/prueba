from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('listado7', views.listado,name='listado'),
    path('register', views.register,name='register'),
]