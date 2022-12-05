from django.urls import path
from orm2 import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),

]
