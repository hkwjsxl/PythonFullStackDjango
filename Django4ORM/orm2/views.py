from django.shortcuts import render, HttpResponse
from orm2.models import *
from django.db.models import Count


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


def query(request):
    """
    关联字段在哪一方，哪一方就是正向，反之就是反向
    正向查询：直接点关联字段
    反向查询：related_name或表名小写_set（一对一直接表名小写）
    """
    """基于模型类对象查询"""
    """一对多查询"""
    # 查询学生hkw所在的班级名称
    # stu_obj = Student.objects.get(name='hkw')
    # print(stu_obj.classes.name)
    # 查询计科1班的所有学生姓名
    # classes_obj = Classes.objects.get(name='计科1班')
    # print(classes_obj.student_set.all())
    # related_name方式
    # classes_obj = Classes.objects.get(name='计科1班')
    # print(classes_obj.classes.all())

    """多对多查询"""
    # 查询学生hkw选修的课程名称
    # stu_obj = Student.objects.get(name='hkw')
    # print(stu_obj.course.all())
    # 查询选修Python全栈的所有学生
    # course_obj = Course.objects.get(name='Python全栈')
    # print(course_obj.student_set.all())
    # course_obj = Course.objects.get(name='Python全栈')
    # print(course_obj.course.all())

    """一对一查询"""
    # 查询学生hkw的手机号
    # stu_obj = Student.objects.get(name='hkw')
    # print(stu_obj.student_detail.phone)
    # 查询手机号为110的学生姓名
    # detail_obj = StudentDetail.objects.get(phone='110')
    # print(detail_obj.student.name)
    # detail_obj = StudentDetail.objects.get(phone='110')
    # print(detail_obj.student_detail.name)
    return HttpResponse('OK')


def query2(request):
    """
    # join查询

    # 查询所有学生的姓名以及所在班级名称
    select db_student.name,db_classes.name from db_student inner join db_classes on db_student.classes_id=db_classes.id

    # 查询所有学生姓名以及选修的课程名称
    select db_student.name,db_course.name from db_student
    inner join db_student2course on db_student.id=db_student2course.student_id
    inner join db_course on db_student2course.course_id = db_course.id
    """
    """基于双下划线的查询"""
    # (1) 查询年龄大于22的学生的姓名以及所在名称班级
    # ret = Student.objects.filter(age__gt=22).values('name', 'classes__name')
    # print(ret)
    # ret = Classes.objects.filter(classes__age__gt=22).values('name', 'classes__name')
    # print(ret)
    # (2) 查询计科1班有哪些学生
    # ret = Classes.objects.filter(name='计科1班').values('name', 'classes__name')
    # print(ret)
    # (3) 查询hkw所报课程的名称
    # ret = Student.objects.filter(name='hkw').values('name', 'course__name')
    # print(ret)
    # (4) 查询选修了Python全栈这门课程学生的姓名和年龄
    # ret = Course.objects.filter(name='Python全栈').values('name', 'course__name', 'course__age')
    # print(ret)
    # (5) 查询alvin的手机号
    # ret = Student.objects.filter(name='alvin').values('name', 'student_detail__phone')
    # print(ret)
    # (6) 查询手机号是112的学生的姓名和所在班级名称
    # ret = StudentDetail.objects.filter(phone='112').values('student_detail__name', 'student_detail__classes__name')
    # print(ret)
    # ret = Student.objects.filter(student_detail__phone='112').values('name', 'classes__name')
    # print(ret)
    return HttpResponse('OK')


def query3(request):
    #  (1)查询每一个班级的名称以及学生个数
    # ret = Classes.objects.values('name').annotate(stu_num=Count('classes__name'))
    # print(ret)
    #  (2)查询每一个学生的姓名,年龄以及选修课程的个数
    # ret = Student.objects.values('name', 'age').annotate(score_num=Count('course__name'))
    # print(ret)
    #  (3)每一个课程名称以及选修学生的个数
    # ret = Course.objects.values('name').annotate(stu_num=Count('course__name'))
    # print(ret)
    #  (4)查询选修课程个数大于1的学生姓名以及选修课程个数
    # ret = Student.objects.values('name').filter(course__name__gt=1).annotate(course_num=Count('course__name'))
    # print(ret)
    #  (5)查询每一个学生的姓名以及选修课程个数并按着选修的课程个数进行从低到高排序
    # ret = Student.objects.values('name', course_num=Count('course__name')).order_by('course_num')
    # print(ret)
    return HttpResponse('OK')
