"""Django5Others URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajax/', include('ajax.urls')),
    path('middleware/', include('middleware.urls')),
    path('cookies_session/', include('cookies_session.urls')),
    # 别名如果发生冲突，未声明命名空间时，不同app下如果有相同的路由别名，反向解析会解析到最下面的app，会发生覆盖
    path('auth_utils/', include(('auth_utils.urls', 'auth_utils'), namespace='auth_utils')),
]
