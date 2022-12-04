from django.urls import path
from orm import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    # 普通查询
    path('query/', views.query),
    # 模糊查询
    path('query2/', views.query2),
    # 高阶查询
    path('query3/', views.query3),
    # 更新和删除
    path('update_delete/', views.update_delete),
]
