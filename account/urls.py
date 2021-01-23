from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.user_profile, name='user_profile'),
	path('index/', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('edit/', views.user_edit, name='user_edit'),
]
