from django.urls import path
from orm2 import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('query/', views.query),
    path('query2/', views.query2),

]
