# Django

- 每一个文件夹都是一个Django项目

- Django1Urls：Django路由

- Django2Views：Django视图

- Django3Templates：Django模板

- Django4ORM：DjangoORM

- Django5Others：Django其他功能

- Django大作业：https://github.com/HkwJsxl/CourseSelSystem

## Django常用命令

### 基本命令

| **任务**                             | **命令**                                                     |
| ------------------------------------ | ------------------------------------------------------------ |
| 创建新项目                           | django-admin.py startproject project_name(注意: windows系统下请用django-admin startproject xxx) |
| 创建新应用                           | python manage.py startapp app_name (注意: 你需要先cd进入创建的项目文件夹) |
| 检测模型变化，生成新的数据库迁移文件 | python manage.py makemigrations [app_name](注意: app名字可选。如果一个项目包含多个app，而你只更改了其中一个app的模型，建议后面加入具体的app名) |
| 同步数据库与模型                     | python manage.py migrate                                     |
| 启动服务器                           | python manage.py runserver                                   |
| 创建超级用户                         | python manage.py createsuperuser                             |
| 修改用户密码                         | python manage.py changepassword username                     |
| 打开交互终端                         | python manage.py shellpython manage.py dbshell(数据库交互)   |
| 查看当前版本                         | python manage.py version                                     |

### 其它命令

| **命令**                               | **用途**                                                     |
| -------------------------------------- | ------------------------------------------------------------ |
| python manage.py flush                 | 清空数据库内容，只留下空表                                   |
| python manage.py test                  | 开始测试                                                     |
| python manage.py collectstatic         | 搜集静态文件                                                 |
| python manage.py createcachetable      | 创建缓存表                                                   |
| python manage.py check                 | 检测项目有没有问题                                           |
| python manage.py inspectdb [table]     | 根据已有数据库反向生成django模型。你可以选择数据表名字       |
| python manage.py makemessages          | 搜集所有的messages，可以生成指定文件格式如xml文件，供后期翻译 |
| python manage.py sendtestemail [email] | 发送测试邮件                                                 |
| python manage.py showmigrations        | 显示所有数据库迁移文件                                       |

## Django常用模块和语句

### 测试脚本

~~~python
# 脚本代码无论是写在应用下的tests.py还是自己单独开设py文件都可以
# 测试环境的准备 去manage.py中拷贝前四行代码 然后自己写两行
import os
import sys
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django5Others.settings')
    import django
    django.setup()
~~~

### base

~~~python
from django.contrib import admin
from django.urls import path, re_path, include
    path('user/', include('user.urls'))  # 路由分发
from django.urls import register_converter
    register_converter(路由转换器的类名, '调用别名')
from django.shortcuts import render, HttpResponse, redirect
    return HttpResponse(data, status=404, content_type='application/json')
    return render(request, 'user/index.html', locals())
    return redirect('/user/')
from django.http import JsonResponse
    JsonResponse(dic, json_dumps_params={'ensure_ascii': False})
    JsonResponse(lst, safe=False)  # 序列化非字典数据类型
from django.views.decorators.http import require_http_methods
    @require_http_methods(["POST"])  # 只接收POST请求
from django.template.loader import get_template
    get_template()  # 获取模板文件
"""自定义过滤器"""
from django import template
    register = template.Library()
    @register.filter('hide_phone')
"""标签"""
{% include 'tem/advertisement.html' %}
{% extends 'tem/base.html' %}
{% block title %}
    {{ block.super }}  # 父级内容
    <title>base</title>
{% endblock title %}
"""反向解析"""
<a href="{% url 'base' %}">Base</a>
from django.urls import reverse
def base(request):
    base_page = reverse('base')
    print('reverse---', base_page)
    return render(request, 'tem/base.html')

"""序列化Queryset"""
from django.core import serializers
ret = models.Book.objects.all()
data = serializers.serialize("json", ret)

"""命名空间：namespace"""
urlpatterns = [
    path('author/', include(('author.urls', 'author'), namespace='author')),
]
{% url 'author:index' %}  # 使用

"""允许转义"""
from django.utils.safestring import mark_safe
res = mark_safe('<h1>xxx</h1>')
<p>转义:{{ ooo|safe }}</p>
<p>转义:{{ res }}</p>

"""查看内部sql语句的方式1(方式2setting.py配置)"""
queryset对象.query

"""默认path转换器"""
str：匹配任何非空字符串，但不含斜杠/，如果你没有专门指定转换器，那么这个是默认使用的；
int：匹配0和正整数，返回一个int类型
slug：可理解为注释、后缀、附属等概念，是url拖在最后的一部分解释性字符。该转换器匹配任何ASCII字符以及连接符和下划线，比如’ building-your-1st-django-site‘；
uuid：匹配一个uuid格式的对象。为了防止冲突，规定必须使用破折号，所有字母必须小写，例如’075194d3-6885-417e-a8a8-6c931e272f00‘ 。返回一个UUID对象；
path：匹配任何非空字符串，重点是可以包含路径分隔符’/‘。这个转换器可以帮助你匹配整个url而不是一段一段的url字符串 
~~~

### 静态文件配置

~~~python
# 我们将网站所使用的静态文件默认都放在static文件夹下
-static
    --js
    --css
    --img
    其他第三方文件
STATIC_URL = '/static/'  # 访问静态文件的令牌
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]
# 静态文件动态解析
{% load static %}
<link rel="stylesheet" href="{% static 'xxx.css' %}">
<script src="{% static 'xxx.js' %}"></script>
~~~

### ORM

~~~python
# 数据库表反向生成模型类
python manage.py inspectdb > models文件名
# 高阶查询
from django.db.models import F, Q, Max, Min, Sum, Count, Avg

详情：https://github.com/HkwJsxl/PythonFullStackDjango/blob/master/Django4ORM/ORM.md
~~~

### Setting.py

~~~python
"""自动加斜杠"""
APPEND_SLASH = True（默认）
"""数据库配置"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'NAME': 'orm',
    }
}
# __init__.py
import pymysql
pymysql.install_as_MySQLdb()
"""ORM打印SQL"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

"""静态资源"""
"""
1 网址所使用的静态文件默认放在static文件夹下
2 用户上传的静态文件也应该单独放在某个文件夹下

media配置
	该配置可以让用户上传的所有文件都固定存放在某一个指定的文件夹下
	# 配置用户上传的文件存储位置
	MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 文件名 随你 自己
	会自动创建多级目录
	
如何开设后端指定文件夹资源
	首先你需要自己去urls.py书写固定的代码
	from django.views.static import serve
	from django.conf import settings  # django默认的配置文件
	# 暴露后端指定文件夹资源
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})
"""

"""用户文件夹路径"""
def user_directory_path(instance, filename):
    return os.path.join('user_dir_path', instance.name, "avatars", filename)

class Userinfo(models.Model):
    name = models.CharField(max_length=32)
    avatar_img = models.FileField(upload_to=user_directory_path)

"""时区时间问题（注释掉）"""
# USE_TZ = True
~~~

## AJAX

~~~python
"""坑：处理完Ajax请求后，可能要刷新页面才能跳转到新的页面"""
"""基础语法"""
$.ajax({
    url: '{% url "register" %}',
    type: 'post',
    data: {
        'csrfmiddlewaretoken': '{{ csrf_token }}'
    },
    success: function (res) {
        
    }
})
"""发送文件"""
"""
ajax发送文件需要借助于js内置对象FormData
"""
<script>
    // 点击按钮朝后端发送普通键值对和文件数据
    $('#btn_submit').on('click',function () {
        // 1 需要先利用FormData内置对象
        let formDateObj = new FormData();
        // 2 添加普通的键值对
        formDateObj.append('username',$('#d1').val());
        formDateObj.append('password',$('#d2').val());
        // 3 添加文件对象
        formDateObj.append('myfile',$('#d3')[0].files[0])
        // 4 将对象基于ajax发送给后端
        $.ajax({
            url:'',
            type:'post',
            data:formDateObj,  // 直接将对象放在data后面即可
            // ajax发送文件必须要指定的两个参数
            contentType:false,  // 不需使用任何编码 django后端能够自动识别formdata对象
            processData:false,  // 告诉你的浏览器不要对你的数据进行任何处理
            success:function (args) {
            }
        })
    })
</script>
"""
总结:
	1.需要利用内置对象FormData
    // 2 添加普通的键值对
        formDateObj.append('username',$('#d1').val());
        formDateObj.append('password',$('#d2').val());
        // 3 添加文件对象
        formDateObj.append('myfile',$('#d3')[0].files[0])
	2.需要指定两个关键性的参数
    	contentType:false,  // 不需使用任何编码 django后端能够自动识别formdata对象
        processData:false,  // 告诉你的浏览器不要对你的数据进行任何处理
	3.django后端能够直接识别到formdata对象并且能够将内部的普通键值自动解析并封装到request.POST中 文件数据自动解析并封装到request.FILES中
"""

# 头像设置
$("#myfile").change(function () {
    // 文件阅读器对象
    // 1 先生成一个文件阅读器对象
    let myFileReaderObj = new FileReader();
    // 2 获取用户上传的头像文件
    let fileObj = $(this)[0].files[0];
    // 3 将文件对象交给阅读器对象读取
    myFileReaderObj.readAsDataURL(fileObj)  // 异步操作，IO操作
    // 4 利用文件阅读器将文件展示到前端页面，修改src属性
    // 等待文件阅读器加载完毕之后再执行
    myFileReaderObj.onload = function(){
         $('#myimg').attr('src',myFileReaderObj.result)
    }
})

~~~

## 中间件

~~~python
MIDDLEWARE = [
    # 一些安全设置，XSS脚本过滤，SSL重定向
    'django.middleware.security.SecurityMiddleware',
    # 数据库迁移时会生成django_session表
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 通用中间件，会处理一些URL，比如baidu.com会自动的处理成www.baidu.com
    'django.middleware.common.CommonMiddleware',
    # 跨域请求伪造中间件，防止CSRF攻击
    'django.middleware.csrf.CsrfViewMiddleware',
    # auth模块相关，向每个接收到的HttpRequest对象添加user属性，表示当前登录的用户。无它用不了request.user
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 开启基于Cookie和会话的消息支持
    'django.contrib.messages.middleware.MessageMiddleware',
    # 对点击劫持的保护
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
~~~

## Auth

~~~python
# 1.比对用户名和密码是否正确
user_obj = auth.authenticate(request,username=username,password=password)
# 括号内必须同时传入用户名和密码
print(user_obj)  # 数据不符合则返回None

# 2.保存用户状态
auth.login(request,user_obj)  # 类似于request.session[key] = user_obj
# 主要执行了该方法 你就可以在任何地方通过request.user获取到当前登陆的用户对象

# 3.判断当前用户是否登陆
request.user.is_authenticated

# 4.获取当前登陆用户
request.user

# 5.校验用户是否登陆装饰器
from django.contrib.auth.decorators import login_required
# 局部配置
@login_required(login_url='/login/')
# 全局配置
LOGIN_URL = '/login/'
1.如果局部和全局都有 该听谁的?
    局部 > 全局
2.局部和全局哪个好呢?
    全局的好处在于无需重复写代码 但是跳转的页面却很单一
    局部的好处在于不同的视图函数在用户没有登陆的情况下可以跳转到不同的页面

# 6.比对原密码
request.user.check_password(old_password)

# 7.修改密码(分两步)
request.user.set_password(new_password)  # 仅仅是在修改对象的属性
request.user.save()  # 这一步才是真正的操作数据库

# 8.注销
auth.logout(request) 

# 9.注册
# 操作auth_user表写入数据
User.objects.create(username=username,password=password)  # 写入数据  不能用create 密码没有加密处理
# 创建普通用户
User.objects.create_user(username=username,password=password)
# 创建超级用户(了解):使用代码创建超级用户 邮箱是必填的 而用命令创建则可以不填
User.objects.create_superuser(username=username,email='123@qq.com',password=password)

"""如何扩展auth_user表"""
from django.contrib.auth.models import User, AbstractUser
class UserInfo(AbstractUser):
    """
    如果继承了AbstractUser
    那么在执行数据库迁移命令的时候auth_user表就不会再创建出来了
    而UserInfo表中会出现auth_user所有的字段外加自己扩展的字段
    这么做的好处在于你能够直接点击你自己的表更加快速的完成操作及扩展
    
    前提:
        1.在继承之前没有执行过数据库迁移命令
            auth_user没有被创建，如果当前库已经创建了那么你就重新换一个库
        2.继承的类里面不要覆盖AbstractUser里面的字段名
            表里面有的字段都不要动，只扩展额外字段即可
        3.需要在配置文件中告诉django你要用UserInfo替代auth_user(******)
            AUTH_USER_MODEL = 'app01.UserInfo'
                                **'应用名.表名'**
    """
    phone = models.CharField()
"""
你如果自己写表替代了auth_user，
那么auth模块的功能还是照常使用，参考的表页由原来的auth_user变成了UserInfo
~~~

## admin后台管理

~~~python
"""
去你的应用下的admin.py中注册你的模型表
from django.contrib import admin
from app01 import models

admin.site.register(models.UserInfo)
admin.site.register(models.Blog)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.Article2Tag)
admin.site.register(models.UpAndDown)
admin.site.register(models.Comment)
"""
class Meta:
    verbose_name_plural = '用户表'  # admin后台表名
# admin会给每一个注册了的模型表自动生成增删改查四条url
http://127.0.0.1:8000/admin/app01/userinfo/  查
http://127.0.0.1:8000/admin/app01/userinfo/add/  增
http://127.0.0.1:8000/admin/app01/userinfo/1/change/  改
http://127.0.0.1:8000/admin/app01/userinfo/1/delete/  删
~~~

## csrf

~~~python
"""csrf中间件会先判断所带数据中有没有token，再去请求头中查找"""
from django.middleware.csrf import get_token
def get_token_value(request):
    return HttpResponse(get_token(request))
$.ajax({
    url: '{% url "csrf:get_token_value" %}',
    success: function (res) {
        localStorage.setItem('csrftoken', res)
    },
})
$('#btn_login').click(function () {
    $.ajax({
        url: '{% url "csrf:login" %}',
        type: 'post',
        data: {
            'username': $('#username').val(),
            'password': $('#password').val(),
            {#'csrfmiddlewaretoken': localStorage.getItem('csrftoken'),#}
        },
        headers: {'X-CSRFToken': localStorage.getItem('csrftoken')},
        success: function (res) {
            location.href = '{% url "csrf:index" %}';
        },
    })
})

"""全局使用，局部禁csrf"""
from django.views.decorators.csrf import csrf_exempt,csrf_protect
@csrf_exempt
def 函数名(request):  # 加上装饰器后,这个视图函数,就没有csrf校验了

from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class index(View):
    def get(self,request):
        return HttpResponse("GET")
    def post(self,request):
        return HttpResponse("POST")
~~~

## forms组件

~~~python
from django import forms


class RegForm(forms.Form):
    username = forms.CharField(
        min_length=3, max_length=8, label='用户名',
        error_messages={
            'min_length': '用户名最少3位',
            'max_length': '用户名最大8位',
            'required': "用户名不能为空"
        },
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        min_length=3, max_length=8, label='密码',
        error_messages={
            'min_length': '密码最少3位!',
            'max_length': '密码最大8位!',
            'required': "密码不能为空!"
        },
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        min_length=3, max_length=8, label='确认密码',
        error_messages={
            'min_length': '确认密码最少3位!',
            'max_length': '确认密码最大8位!',
            'required': "确认密码不能为空!"
        },
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='邮箱',
        error_messages={
            'invalid': '邮箱格式不正确!',
            'required': "邮箱不能为空!"
        },
        initial='test@test.com',
        widget=forms.widgets.EmailInput(attrs={'class': 'form-control'})
    )

    # 局部钩子
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username in ['admin', '管理员']:
            self.add_error('username', '用户名不合法!')
        return username

    # 全局钩子
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password != password:
            self.add_error('confirm_password', '两次密码不一致!')
        return self.cleaned_data

~~~

## 扩展

~~~python
Jquery插件：https://www.jq22.com/
AJAX弹窗：https://sweetalert2.github.io/
~~~
