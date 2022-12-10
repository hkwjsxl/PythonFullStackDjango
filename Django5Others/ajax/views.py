from django.shortcuts import render, HttpResponse, reverse
from ajax.models import UserInfo
from django.http import JsonResponse
from ajax.utils import md5_enc


# Create your views here.
def register(request):
    if request.method == 'POST':
        res_dict = {'status': 2000, 'msg': ''}
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = md5_enc(password)
        user = UserInfo.objects.filter(username=username)
        if user:
            res_dict['status'] = 4000
            res_dict['msg'] = '用户名已存在!'
        else:
            UserInfo.objects.create(username=username, password=password)
            res_dict['msg'] = '注册成功!'
        return JsonResponse(res_dict)
    return render(request, 'ajax/register.html', locals())


def cacl(request):
    if request.method == 'POST':
        num1 = eval(request.POST.get('num1'))
        num2 = eval(request.POST.get('num2'))
        return HttpResponse(str(num1 + num2))
    return render(request, 'ajax/cacl.html', locals())


def show_user(request):
    user_queryset = UserInfo.objects.all()

    return render(request, 'ajax/show_user.html', locals())
