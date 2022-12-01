from django.urls import path, re_path, include
from article import views

urlpatterns = [
    path('', views.index),
    re_path('(?P<year>\d{4})/(?P<month>\d{1,2})', views.article),
]
