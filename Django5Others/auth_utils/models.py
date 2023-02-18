from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    # 扩展字段
    phone = models.CharField(max_length=11, db_index=True, verbose_name='手机号')

    class Meta:
        db_table = 'auth_userinfo'

