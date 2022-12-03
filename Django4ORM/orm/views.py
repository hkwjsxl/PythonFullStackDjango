from django.shortcuts import render, HttpResponse
from orm.models import Stu


# Create your views here.
def index(request):
    return render(request, 'orm/index.html')


def add(request):
    # 方法一
    # stu_obj = Stu(name='hkw', age=21, sex=1, classmate='Python全栈', description='代码改变生活')
    # stu_obj.save()
    # 方法二
    stu_obj = Stu.objects.create(name='alvin', age=20, sex=0, classmate='Linux')
    # stu_obj = Stu.objects.create(name='lin', age=20, sex=1, classmate='Linux')
    # stu_obj = Stu.objects.create(name='li', age=20, sex=1, classmate='Linux')
    # stu_obj = Stu.objects.create(name='liu', age=20, sex=2, classmate='Linux')

    print(stu_obj.id, stu_obj.name, stu_obj.classmate)

    return HttpResponse('添加成功')


def query(request):
    """查询API"""
    # 1.all
    # stu_queryset = Stu.objects.all()
    # print(stu_queryset)

    # 2.first
    # stu_obj = Stu.objects.first()
    # print(stu_obj)

    # 3.last
    # stu_obj = Stu.objects.last()
    # print(stu_obj)

    # 4.filter
    # stu_queryset = Stu.objects.filter(pk=1)
    # print(stu_queryset)

    # 5.exclude
    # stu_queryset = Stu.objects.exclude(pk=1)
    # print(stu_queryset)

    # 6.get(返回结果有且只有一个,(过多或没有都会报错))
    # stu_obj = Stu.objects.get(pk=1)
    # print(stu_obj)

    # 7.order_by
    # stu_queryset = Stu.objects.all().order_by('-age', '-id')
    # print(stu_queryset)

    # 8.count
    # count = Stu.objects.all().count()
    # print(count)

    # 9.exists
    # is_exists = Stu.objects.exists()
    # print(is_exists)

    # 10.values, values_list
    # stu_queryset = Stu.objects.all().values('name', 'age')
    # print(stu_queryset, type(stu_queryset.first()))  # 列表套字典
    # stu_queryset = Stu.objects.all().values_list('name', 'age')
    # print(stu_queryset, type(stu_queryset.first()))  # 列表套元组

    # 11.distinct
    # stu_queryset = Stu.objects.values('age').distinct()
    # print(stu_queryset)

    return HttpResponse('查询成功')
