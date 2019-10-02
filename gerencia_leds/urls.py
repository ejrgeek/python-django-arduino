from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('ligar/', led_on, name='led_on'),
    path('desligar/', led_off, name='led_off'),
]