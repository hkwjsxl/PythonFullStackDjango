from django.shortcuts import render, HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'app01/index.html')


def current_time(request):
    now_time = datetime.now().strftime('%Y-%m-%d %X')
    return HttpResponse(now_time)


def article(request, year, month):
    return HttpResponse(f'{year}-{month}---文章')


def mobile(request, phone):
    print('mobile', phone, type(phone))
    return HttpResponse(f'{phone}')
