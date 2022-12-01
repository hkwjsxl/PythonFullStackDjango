import json

from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse


# Create your views here.
def index(request):
    # 请求方法
    # print(request.method)
    # 获取get数据
    # print(request.GET)
    # 获取请求头数据
    # print(request.META)
    # print('IP Addr:', request.META.get('REMOTE_ADDR'))
    # 获取请求体数据
    # print(request.body)
    # 获取请求体数据中的urlencoded数据(---JSON数据获取不到---)
    # print(request.POST)
    # print(request.POST.get('user'))  # hkw
    # print(request.POST.getlist('hobby'))  # ['football', 'basketball']

    # 获取请求路径
    # print(request.path)  # /user/
    # print(request.path_info)  # /user/
    # print(request.get_full_path())  # /user/?age=18

    return HttpResponse('user index')


def http_res(request):
    """content_type=None, status=None, reason=None, charset=None, headers=None"""
    # res = HttpResponse('OK')
    # 返回状态码
    # res = HttpResponse('OK', status=404)
    # 数据类型
    # data = json.dumps({'user': 'hkw'})
    # res = HttpResponse(data, content_type='application/json')  # JSON
    # res = HttpResponse('<h3>OK</h3>', content_type='text/plain')  # 纯文本
    # 自定义响应头
    res = HttpResponse('OK')
    res['user'] = 'hkw'

    return res


def json_res(request):
    dic = {
        'user': 'hkw',
        'hobby': '篮球',
    }
    # res = JsonResponse(dic)
    # 显示中文
    # res = JsonResponse(dic, json_dumps_params={'ensure_ascii': False})

    # 响应非字典类型
    lst = [
        {'user': 'hkw'},
        {'user': 'alvin'},
    ]
    res = JsonResponse(lst, safe=False)
    return res


def render_res(request):
    ip = request.META.get('REMOTE_ADDR')
    # res = render(request, 'user/index.html', {'ip': ip})
    res = render(request, 'user/index.html', locals())
    return res


def redirect_res(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'hkw' and pwd == '123':
            return redirect('/user/')
        msg = '用户名或密码错误!'
        return HttpResponse(msg)
    res = render(request, 'user/login.html', locals())
    return res


@require_http_methods(["POST"])
def login(request):
    """
    Method Not Allowed (GET): /user/login/
    只能接收POST请求
    :param request:
    :return:
    """
    return HttpResponse('login success')
