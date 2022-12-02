from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import get_template
from django.urls import reverse

from datetime import datetime


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return self.title


# Create your views here.
def index(request):
    user = 'hkw'
    age = 21
    user_list = ['hkw', 'jon', 'alvin', 'tom']
    user_dict = {
        'user': 'hkw',
        'age': 18,
    }
    big_list = [{'book': 'Python全栈'}, {'book': 'Linux'}]
    book_obj = Book('Python全栈', 9999)

    current_time = datetime.now()
    file_size = 666666
    content = 'I am a student!'
    link = '<a href="http://www.baidu.com">baidu.com</a>'
    default = ''
    word = 'hello DTL'

    # 自定义过滤器
    phone = 18533538210
    return render(request, 'tem/index.html', locals())


def base(request):
    # return render(request, 'tem/base.html')
    # 反向解析
    base_page = reverse('base')
    print('reverse---', base_page)
    return render(request, 'tem/base.html')


def home(request):
    home_page = reverse('home')
    print('reverse---', home_page)
    return render(request, 'tem/home.html')


def order(request):
    order_page = reverse('order')
    print('reverse---', order_page)
    return render(request, 'tem/order.html')
