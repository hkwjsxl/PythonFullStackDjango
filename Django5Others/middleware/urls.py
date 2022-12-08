from django.urls import path
from middleware import views

urlpatterns = [
    path('', views.index, name='index'),
]
