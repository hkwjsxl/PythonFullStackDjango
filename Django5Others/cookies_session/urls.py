from django.urls import path
from cookies_session import views

urlpatterns = [
    path('', views.index, name='index'),
    # cookie
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # session
    path('index2/', views.index2, name='index2'),
    path('login2/', views.login2, name='login2'),
    path('logout2/', views.logout2, name='logout2'),
]
