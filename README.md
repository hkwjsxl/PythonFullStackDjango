# Django

- 每一个文件夹都是一个Django项目

- Django1Urls：Django路由

- Django1Views：Django视图

- Django1Templates：Django模板

## Django常用模块和语句

~~~python
from django.contrib import admin
from django.urls import path, re_path, include
    path('user/', include('user.urls'))  # 路由分发
from django.urls import register_converter
    register_converter(路由转换器的类名, '调用别名')
from django.shortcuts import render, HttpResponse, redirect
    return HttpResponse(data, status=404, content_type='application/json')
    return render(request, 'user/index.html', locals())
    return redirect('/user/')
from django.http import JsonResponse
    JsonResponse(dic, json_dumps_params={'ensure_ascii': False})
    JsonResponse(lst, safe=False)  # 序列化非字典数据类型
from django.views.decorators.http import require_http_methods
    @require_http_methods(["POST"])  # 只接收POST请求
from django.template.loader import get_template
    get_template()  # 获取模板文件
"""自定义过滤器"""
from django import template
    register = template.Library()
    @register.filter('hide_phone')
"""标签"""
{% include 'tem/advertisement.html' %}
{% extends 'tem/base.html' %}
{% block title %}
    {{ block.super }}  # 父级内容
    <title>base</title>
{% endblock title %}
"""反向解析"""
<a href="{% url 'base' %}">Base</a>
from django.urls import reverse
def base(request):
    base_page = reverse('base')
    print('reverse---', base_page)
    return render(request, 'tem/base.html')
~~~

Setting.py

~~~python
"""自动加斜杠"""
APPEND_SLASH = True（默认）
"""数据库配置"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'NAME': 'orm',
    }
}
# __init__.py
import pymysql
pymysql.install_as_MySQLdb()
~~~

