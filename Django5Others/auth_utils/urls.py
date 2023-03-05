from django.urls import path
from auth_utils import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # MySQL读写分离测试
    path('home/', views.home, name='home'),
]
