from django.db import models


class Classes(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='班级名称')

    class Meta:
        db_table = 'db_classes'


class Course(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='课程名称')

    class Meta:
        db_table = 'db_course'


class Student(models.Model):
    name = models.CharField(max_length=32, verbose_name='学生姓名')
    age = models.SmallIntegerField(default=18, verbose_name='学生年龄')
    # 一对多
    classes = models.ForeignKey(to='Classes', on_delete=models.CASCADE, db_constraint=False, related_name='classes')
    # 多对多，自动创建第三张表
    course = models.ManyToManyField(to='Course', db_table='db_student2course', db_constraint=False, related_name='course')
    # 一对一
    student_detail = models.OneToOneField(to='StudentDetail', on_delete=models.CASCADE, db_constraint=False, related_name='student_detail')

    class Meta:
        db_table = 'db_student'

    def __str__(self):
        return f'学生姓名：{self.name}'


class StudentDetail(models.Model):
    addr = models.CharField(max_length=64, null=True, blank=True, verbose_name='学生地址')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='学生手机号')
    email = models.EmailField(null=True, blank=True, verbose_name='学生邮箱')
    description = models.TextField(null=True, blank=True, verbose_name='学生描述')

    class Meta:
        db_table = 'db_student_detail'
