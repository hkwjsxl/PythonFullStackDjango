from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from cookies_session import models
from django.http import JsonResponse
from cookies_session.utils import COOKIES_SALT, SESSION_SALT

from datetime import datetime


# Create your views here.
def index(request):
    try:
        is_login = request.get_signed_cookie('is_login', salt=COOKIES_SALT)
    except Exception as e:
        print(e)
        print('登录错误')
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
        res.set_signed_cookie('is_login', username, salt=COOKIES_SALT)
        return res
    return render(request, 'cookies_session/login.html')


def logout(request):
    """坑：处理完ajax请求后要刷新页面"""
    res = redirect('login')
    res.delete_cookie('is_login')
    return res


def index2(request):
    is_login = request.session.get('is_login_pk')
    if not is_login:
        return redirect('login2')
    last_login_time = request.session.get('last_login_time', '第一次登录!')
    new_login_time = datetime.now().strftime('%Y-%m-%d %X')
    request.session['last_login_time'] = new_login_time
    return render(request, 'cookies_session/index2.html', {'last_login_time': last_login_time})


def login2(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
        if not user_obj:
            return HttpResponse('用户名或密码错误!')
        request.session['is_login_pk'] = user_obj.pk
        return redirect('index2')
    return render(request, 'cookies_session/login2.html')


def logout2(request):
    # 方式一
    # request.session.flush()
    # 方式二
    del request.session['is_login_pk']

    return redirect('login2')
