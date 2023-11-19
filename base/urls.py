from django.contrib import admin
from django.urls import path, include
from .views import (
    event_list,
    event_detail,
    event_registration,
    user_dashboard,
)


urlpatterns = [
    path('', event_list, name='event_list'),
    path('events/<int:pk>/', event_detail, name='event_detail'),
    path('events/<int:pk>/register/', event_registration, name='event_registration'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    # Add more URLs as needed
]
