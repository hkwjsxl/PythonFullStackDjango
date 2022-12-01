from django.contrib import admin
from django.urls import path, re_path, include
from app01 import views as app01_view
from django.urls import register_converter


class MobileConverter:
    regex = "1[3-9]\d{9}"

    def to_python(self, value):
        print('to_python', value, type(value))
        # 将匹配结果传递到视图内部时使用
        # 返回str还是int主要看需求,纯数字的可以返回int
        if value.isdecimal():
            return int(value)
        return value

    def to_url(self, value):
        # 将匹配结果用于反向解析传值时使用
        return value


# register_converter(路由转换器的类名,调用别名)
register_converter(MobileConverter, "mobile")

urlpatterns = [
    path("admin/", admin.site.urls),
    # 返回当前时间
    # 请求路径和视图函数不是一对一映射关系！
    path('current_time/', app01_view.current_time),
    path('timer/', app01_view.current_time),

    # 无名分组
    # re_path('article/(\d{4})/(\d{1,2})', app01_view.article),
    # 有名分组
    # re_path('article/(?P<year>\d{4})/(?P<month>\d{1,2})', app01_view.article),

    # 路由分发（以index开头的都去找app01）
    path('index/', include('app01.urls')),
    path('article/', include('article.urls')),

    # 路由转发器（自定义转换器）
    path('<mobile:phone>', app01_view.mobile)
]
