from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajax/', include('ajax.urls')),
    path('middleware/', include('middleware.urls')),
    path('cookies_session/', include('cookies_session.urls')),
    # 别名如果发生冲突，未声明命名空间时，不同app下如果有相同的路由别名，反向解析会解析到最下面的app，会发生覆盖
    path('auth_utils/', include(('auth_utils.urls', 'auth_utils'), namespace='auth_utils')),
    path('paginator/', include(('paginator.urls', 'paginator'), namespace='paginator')),
    path('cbv/', include(('cbv.urls', 'cbv'), namespace='cbv')),
    # 前后端分离
    path('csrf/', include(('csrf.urls', 'csrf'), namespace='csrf')),
]
