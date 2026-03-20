from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather, name='weather'),
    path('history/', views.weather_history, name='weather_history'),
    path('about/', views.about, name='about'),
]
