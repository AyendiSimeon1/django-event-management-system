from django.contrib import admin
from django.urls import path, include
from .views import (
    event_list,
    event_detail,
    event_registration,
    user_dashboard,
    create_event,
    update_event,
    delete_event,
    category_detail,
)


urlpatterns = [
    path('', event_list, name='event_list'),
    path('events/create_event/', create_event, name='create_event'),
    path('events/<slug:slug>/', event_detail, name='event_detail'),
    
    path('events/<slug:slug>/register/', event_registration, name='event_registration'),
    
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('<slug:category_slug>/', event_list, name='event_list_by_category'),
    path('events/update_event/<slug:slug>/', update_event, name='update_event'),
    path('events/delete_event/<slug:slug>/', delete_event, name='delete_event'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
  
]
