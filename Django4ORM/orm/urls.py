from django.urls import path
from orm import views
urlpatterns = [
    path('', views.index),
]
