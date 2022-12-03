from django.urls import path
from orm import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('query/', views.query),
]
