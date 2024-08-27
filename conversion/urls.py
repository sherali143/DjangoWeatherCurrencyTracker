from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('exchange_rate/', views.index, name='index'),
    path('convert/', views.currency_convert, name='currency_convert'),
    path('weather/', views.weather_update, name='weather_update')
]
