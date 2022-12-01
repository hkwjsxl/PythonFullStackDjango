from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'article/index.html')


def article(request, year, month):
    return HttpResponse(f'{year}-{month}---文章')
