from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.middleware.csrf import get_token


def index(request):
    return HttpResponse('index')


def login(request):
    if request.method == 'POST':
        return HttpResponse('OK')
    return render(request, 'csrf/login.html')


def get_token_value(request):
    return HttpResponse(get_token(request))
