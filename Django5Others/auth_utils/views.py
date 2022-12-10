from django.shortcuts import render, HttpResponse, redirect, reverse
from auth_utils import models
from django.db import transaction
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def login_auth(func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        current_url = request.path_info
        login_url = reverse('auth_utils:login') + f'?next_url={current_url}'
        """
        前端提交表单地址不能写action='{% url "auth_utils:login" %}'
        直接action=""
        """
        return redirect(login_url)

    return inner


@login_auth
def index(request):
    return render(request, 'auth_utils/index.html', {'request': request})


def register(request):
    if request.is_ajax():
        if request.method == 'POST':
            res_dic = {'status': 2000, 'msg': '注册成功!'}
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                with transaction.atomic():
                    user_obj = models.UserInfo.objects.filter(username=username)
                    if user_obj:
                        res_dic['status'] = 4000
                        res_dic['msg'] = '用户已存在!'
                        return JsonResponse(res_dic)
                    models.UserInfo.objects.create_user(username=username, password=password)
                    return JsonResponse(res_dic)
            except Exception as e:
                print(e)
                res_dic['status'] = 4000
                res_dic['msg'] = '服务器错误!'
                return JsonResponse(res_dic)
    return render(request, 'auth_utils/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = auth.authenticate(request, username=username, password=password)
        if user_obj:
            next_url = request.GET.get('next_url')
            auth.login(request, user_obj)
            if next_url:
                return redirect(next_url)
            return redirect('auth_utils:index')
        return HttpResponse('用户名或密码错误!')
    return render(request, 'auth_utils/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponse('注销成功')
