from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='api_login_user'),
    path('signup', views.signup, name='api_signup'),
    path('signup_store/<slug:username>/', views.signup_store, name='api_signup_store'),
    path('signup_store_auth/', views.signup_store_auth, name='api_signup_store_auth'),
]