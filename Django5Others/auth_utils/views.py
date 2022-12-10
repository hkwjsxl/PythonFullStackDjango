from django.shortcuts import render, HttpResponse, redirect, reverse


# Create your views here.
def index(request):
    ret = reverse('auth_utils:index')
    print(ret)
    return render(request, 'auth_utils/index.html')


def register(request):
    return render(request, 'auth_utils/register.html')


def login(request):
    return render(request, 'auth_utils/login.html')


def logout(request):
    return HttpResponse('注销成功')
