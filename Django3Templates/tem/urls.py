from django.urls import path, include
from tem import views

urlpatterns = [
    path('', views.index)
]
