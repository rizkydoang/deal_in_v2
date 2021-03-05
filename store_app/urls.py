from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('index_store/<slug:id_store>/', views.index_store, name='api_index_store'),
    path('index_home/', views.index_home, name='api_index_home'),
]
