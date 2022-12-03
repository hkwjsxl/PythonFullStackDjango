from django.db import models


# Create your models here.
class Stu(models.Model):
    # 自动生成主键字段(ID)，后续较多使用pk自动查找主键

    SEX_CHOICE = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    )
    # db_index创建数据库索引，unique唯一索引
    name = models.CharField(max_length=32, db_index=True, unique=True, verbose_name='姓名')
    age = models.SmallIntegerField(default=18, verbose_name='年龄')
    sex = models.SmallIntegerField(choices=SEX_CHOICE, default=2, verbose_name='性别')
    # auto_now_add和auto_add首次创建都会入库当前时间
    # auto_now_add 当数据添加时设置当前时间为默认值
    # auto_now= 当数据添加/更新时, 设置当前时间为默认值
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # db_column数据库中的列名
    classmate = models.CharField(db_column='class', max_length=8, db_index=True, default='', verbose_name='班级')
    description = models.TextField(verbose_name='个性签名', default='')

    # class Meta:
    #     # 指定表名，默认为app名小写_类名小写
    #     db_table = 'student'
    #     # 在admin站点中显示的名称
    #     verbose_name = '学生信息表'
    #     # 显示的复数名称
    #     verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

