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
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Index
    path('', views.index, name='home'),


    # Authentication Store & Sign - Up Store
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout, name='logout_user'),
    path('signup/', views.signup, name='signup_user'),
    path('signup_store/', views.signup_store, name='signup_store'),
    path('pin_store/', views.signup_store_auth, name='pin_store_auth'),

    # Store App
    path('store/index/<slug:id_store>/', views.index_store, name='index_store'),
    path('store/add_item/', views.add_item, name='add_item_store'),
    path('store/delete_item/', views.delete_item, name='delete_item_store'),


    # API Microservice Deal_In
    path('api/auth/', include('auth_app.urls')),
    path('api/user/', include('profile_app.urls')),
    path('api/store/', include('store_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
