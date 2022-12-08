from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from cookies_session import models
from django.http import JsonResponse
from cookies_session.utils import COOKIES_SALT


# Create your views here.
def index(request):
    try:
        is_login = request.get_signed_cookie('is_login')
    except Exception as e:
        return redirect('login')
    return render(request, 'cookies_session/index.html', {'is_login': is_login})


def register(request):
    if request.method == 'POST':
        res_dict = {'status': 2000, 'message': '注册成功!'}
        user = request.POST.get('username')
        user_obj = models.UserInfo.objects.filter(username=user).first()
        if user_obj:
            res_dict['status'] = 4000
            res_dict['message'] = f'{user}---已存在!'
            return JsonResponse(res_dict)
        pwd = request.POST.get('password')
        models.UserInfo.objects.create(username=user, password=pwd)
        return JsonResponse(res_dict)

    return render(request, 'cookies_session/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
        if not user_obj:
            return HttpResponse('用户名或密码错误!')
        res = redirect('index')
        res.set_signed_cookie('is_login', username)
        return res
    return render(request, 'cookies_session/login.html')


def logout(request):
    """坑：处理完ajax请求后要刷新页面"""
    res = redirect('login')
    res.delete_cookie('is_login')
    return res
