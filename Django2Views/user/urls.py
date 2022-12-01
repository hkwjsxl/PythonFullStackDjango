from django.urls import path, re_path, include
from user import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('http_res/', views.http_res),
    path('json_res/', views.json_res),
    path('render_res/', views.render_res),
    path('redirect_res/', views.redirect_res),
]
