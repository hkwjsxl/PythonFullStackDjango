from django.urls import path
from orm2 import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    # 基于模型类对象查询
    path('query/', views.query),
    # 基于双下划线的查询
    path('query2/', views.query2),
    # 关联分组查询
    path('query3/', views.query3),

]
