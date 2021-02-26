from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<slug:id>/', views.detail, name='api_detail_user'),
]
