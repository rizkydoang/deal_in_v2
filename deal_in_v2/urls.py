"""deal_in_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Index
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),


    # Authentication Store & Sign - Up Store
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout, name='logout_user'),
    path('signup/', views.signup, name='signup_user'),
    path('signup_store/', views.signup_store, name='signup_store'),
    path('pin_store/', views.signup_store_auth, name='pin_store_auth'),

    # Store App
    path('store/', views.index_store, name='index_store'),


    # API Microservice Deal_In
    path('api/auth/', include('auth_app.urls')),
    path('api/user/', include('profile_app.urls')),
    path('api/store/', include('store_app.urls')),
]
