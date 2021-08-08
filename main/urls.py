from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('add/', views.add, name = 'views-main'),
    path('commands/', views.commands, name = 'commands-main'),
    path('about/', views.about, name = 'about-main'),
    path('', views.home, name = 'home-main'),
]