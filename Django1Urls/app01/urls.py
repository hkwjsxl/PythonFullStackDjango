from django.urls import path, re_path, include
from app01 import views

urlpatterns = [
    path('', views.index),
]
