from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='api_login_user'),
    path('signup', views.signup, name='api_signup'),
]