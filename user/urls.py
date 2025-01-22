from django.contrib import admin
from django.urls import path, include
from .views import UserCreateView
urlpatterns = [
    path('singup/', UserCreateView.as_view(), name="singup")
]