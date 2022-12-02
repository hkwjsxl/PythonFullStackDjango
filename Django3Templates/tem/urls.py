from django.urls import path, include
from tem import views

urlpatterns = [
    path('', views.index),
    # 反向解析,name=
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('order/', views.order, name='order'),
]
