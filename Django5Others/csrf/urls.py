from django.urls import path
from csrf import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('get_token_value/', views.get_token_value, name='get_token_value'),
]
