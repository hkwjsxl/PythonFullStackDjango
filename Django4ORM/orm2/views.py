from django.shortcuts import render, HttpResponse
from orm2.models import *


# Create your views here.
def index(request):
    return HttpResponse('orm2')


def add(request):
    # Classes.objects.create(name='计科1班')
    # Classes.objects.create(name='计科2班')
    # Classes.objects.create(name='网安1班')
    # Classes.objects.create(name='网安2班')
    # Course.objects.create(name='Python全栈')
    # Course.objects.create(name='linux')
    # Course.objects.create(name='go')
    # Course.objects.create(name='Java')
    # Course.objects.create(name='C#')
    # StudentDetail.objects.create(addr='北京')
    # StudentDetail.objects.create(addr='上海')
    # StudentDetail.objects.create(addr='广东')
    # StudentDetail.objects.create(addr='深圳')
    # StudentDetail.objects.create(addr='河北')

    # Student.objects.create(name='hkw', age=21, classes_id=1, student_detail_id=1)
    # Student.objects.create(name='jon', age=20, classes_id=1, student_detail_id=2)
    # Student.objects.create(name='alvin', age=22, classes_id=2, student_detail_id=3)
    # Student.objects.create(name='lin', age=20, classes_id=3, student_detail_id=4)
    # stu = Student.objects.create(name='li', age=23, classes_id=4, student_detail_id=5)
    # print(stu, type(stu))

    """多对多添加记录"""
    # # 方式一
    # stu_obj = Student.objects.get(pk=1)
    # c1 = Course.objects.get(pk=1)
    # c2 = Course.objects.get(pk=2)
    # stu_obj.course.add(c1, c2)
    # # 方式二
    # stu_obj = Student.objects.get(pk=2)
    # stu_obj.course.add(1, 2, 3)
    # # 方式三
    # stu_obj = Student.objects.get(pk=3)
    # stu_obj.course.add(*[1, 2, 3])

    # stu_obj = Student.objects.get(pk=3)
    # remove方法，删除记录
    # stu_obj.course.remove(3)
    # clear方法，清空记录
    # stu_obj.course.clear()
    # set方法，重置
    # stu_obj.course.set([3, 4, 5])
    # all方法，查询
    # 查询hkw的所选课程
    # stu_obj = Student.objects.get(name='hkw')
    # course_queryset = stu_obj.course.all()
    # print(course_queryset)

    return HttpResponse('OK')
