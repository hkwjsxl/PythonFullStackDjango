from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    print('middleware index')
    return HttpResponse('middleware index')
