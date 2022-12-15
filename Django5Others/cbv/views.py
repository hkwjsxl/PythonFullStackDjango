from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.serializers import serialize
from cbv import models


class BookView(View):
    def get(self, reqeust):
        book_queryset = models.Book.objects.all()
        book_list = serialize('json', book_queryset)
        return HttpResponse(book_list, content_type='json')

    def post(self, reqeust):
        return HttpResponse('cbv get')
