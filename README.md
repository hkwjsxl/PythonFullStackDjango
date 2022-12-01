# Django

- 每一个文件夹都是一个Django项目

- Django1Urls：Django路由

- Django1Views：Django视图

- Django1Templates：Django模板层

## Django常用模块和语句

~~~python
from django.contrib import admin
from django.urls import path, re_path, include
	path('user/', include('user.urls'))  # 路由分发
from django.shortcuts import render, HttpResponse, redirect
	return HttpResponse(data, status=404, content_type='application/json')
	return render(request, 'user/index.html', locals())
from django.http import JsonResponse
	JsonResponse(dic, json_dumps_params={'ensure_ascii': False})
    JsonResponse(lst, safe=False)  # 序列化非字典数据类型
from django.views.decorators.http import require_http_methods
	@require_http_methods(["POST"])  # 只接收POST请求

~~~

Setting.py

~~~python
# 自动加斜杠
APPEND_SLASH = True（默认）

~~~

