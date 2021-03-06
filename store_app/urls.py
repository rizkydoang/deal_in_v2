from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('index_store/<slug:id_store>/', views.index_store, name='api_index_store'),
    path('index_home/', views.index_home, name='api_index_home'),
    path('delete_item/', views.delete_item, name='api_delete_item'),
    path('update_item/', views.update_item, name='api_update_item'),
]
