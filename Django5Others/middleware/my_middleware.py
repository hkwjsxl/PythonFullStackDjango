from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class MyMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        print('MyMiddleware1 request')
        return None

    def process_response(self, request, response):
        print('MyMiddleware1 response')
        return response


class MyMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        print('MyMiddleware2 request')
        return None

    def process_response(self, request, response):
        print('MyMiddleware2 response')
        return response


class VerifyIP(MiddlewareMixin):
    def process_request(self, request):
        print('VerifyIP request')
        # print(request.META)
        user_ip = request.META.get('REMOTE_ADDR')
        if user_ip in ['127.0.0.1']:
            print('黑名单')
            return HttpResponse('黑名单')

        return None
