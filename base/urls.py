from django.contrib import admin
from django.urls import path, include
from base.views import home

urlpatterns = [
    path('', home, name='home'),
    
]