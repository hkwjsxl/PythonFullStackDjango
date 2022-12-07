from django.urls import path
from ajax import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # 案例1，计算器
    path('cacl/', views.cacl, name='cacl'),
    # 案例2，ajax通过orm获取用户数据并展示
    path('show_user/', views.show_user, name='show_user'),
]
