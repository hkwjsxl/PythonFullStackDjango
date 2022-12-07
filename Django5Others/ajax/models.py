from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32, db_index=True, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

