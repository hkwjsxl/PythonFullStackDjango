from django.urls import path
from cbv import views

urlpatterns = [
    path('', views.BookView.as_view(), name='book_view'),
    # path('', 返回值是View类中的view函数, name='book_view'),
]
