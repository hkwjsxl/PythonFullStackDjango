from django.shortcuts import render, HttpResponse
from orm.models import Stu
from django.db.models import F, Q, Max, Min, Sum, Count, Avg


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

    # 12.reverse
    stu_queryset = Stu.objects.all().reverse()
    print(stu_queryset)

    return HttpResponse('查询成功')


def query2(request):
    """模糊查询"""
    # 前加i表示不区分大小写，PS：iexact、icontains、istartswith、iendswith
    # contains,查询名称中带有 l 的记录
    # stu_queryset = Stu.objects.filter(name__contains='l')
    # print(stu_queryset)
    # startswith,查询名称中以 l 开头的记录
    # stu_queryset = Stu.objects.filter(name__startswith='l')
    # print(stu_queryset)
    # endswith,查询名称中以 l 结尾的记录
    # stu_queryset = Stu.objects.filter(name__endswith='l')
    # print(stu_queryset)

    # description,查询描述不为空的记录
    # stu_queryset = Stu.objects.filter(description__isnull=False)
    # print(stu_queryset)

    # range,查询区间内的记录(between and)
    # stu_queryset = Stu.objects.filter(age__range=(20, 30))
    # print(stu_queryset)

    # in,查询in内的记录
    # stu_queryset = Stu.objects.filter(age__in=(18, 20, 21))
    # print(stu_queryset)

    # gt,lt,gte,lte(大于，大于等于)
    # age大于等于20的记录
    # stu_queryset = Stu.objects.filter(age__gte=20)
    # print(stu_queryset)

    # 日期查询
    # 2021年
    # stu_queryset = Stu.objects.filter(create_time__year=2021)
    # print(stu_queryset)
    # 大于大于2021年
    # stu_queryset = Stu.objects.filter(create_time__year__gte=2021)
    # print(stu_queryset)

    return HttpResponse('模糊查询成功')


def query3(request):
    # F查询，两个属性之间的比较
    # 查询语文成绩大于数学成绩的记录
    # ret_queryset = Stu.objects.filter(chinese_score__gt=F('math_score'))
    # print(ret_queryset)

    # Q查询，and，or，not
    # 查询年龄大于30或性别为女的记录
    # ret_queryset = Stu.objects.filter(Q(age__gt=30) | Q(sex=2))
    # print(ret_queryset)
    # 年龄小于19或者大于20的记录
    # ret_queryset = Stu.objects.filter(Q(age__lt=19)|Q(age__gt=20))
    # print(ret_queryset)

    # 聚合查询,aggregate
    # 查询性别为女的数学成绩平均值
    # ret_queryset = Stu.objects.filter(sex=2).aggregate(math_avg=Avg('math_score'))
    # print(ret_queryset)

    # 分组查询,annotate
    # 查询不同性别学生的数学平均成绩
    # ret_queryset = Stu.objects.values('sex').annotate(math_avg=Avg('math_score'))
    # print(ret_queryset)
    # <QuerySet [{'sex': 1, 'math_avg': 80.0}, {'sex': 0, 'math_avg': 80.0}, {'sex': 2, 'math_avg': 80.0}]>
    # 查询每个班级学生的数学平均成绩
    # ret_queryset = Stu.objects.values('classmate').annotate(math_avg=Avg('math_score'))
    # print(ret_queryset)

    # 原生查询
    # ret = Stu.objects.raw('select * from orm.orm_stu;')
    # print(ret, type(ret))  # <RawQuerySet: select * from orm.orm_stu;> <class 'django.db.models.query.RawQuerySet'>
    # for item in ret:
    #     print(item, type(item))   # hkw <class 'orm.models.Stu'>

    return HttpResponse('高阶查询成功')


def update_delete(request):
    """更新"""
    # 方式一，模型类操作，效率低（其他没动的字段也要重新的赋值一遍）
    # stu_obj = Stu.objects.get(pk=1)
    # stu_obj.math_score = 100
    # stu_obj.save()
    # 方式二，queryset对象
    # ID大于5的记录数学成绩降低5分
    # effect_count = Stu.objects.filter(pk__gt=5).update(math_score=F('math_score') - 5)
    # print(effect_count)

    """删除"""
    # del_count = Stu.objects.filter(pk__gt=6).delete()
    # print(del_count)  # (1, {'orm.Stu': 1})

    return HttpResponse('OK')
