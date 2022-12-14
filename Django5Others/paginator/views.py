from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from auth_utils import models


# Create your views here.
def index(request):
    """批量插入数据"""
    # lst = []
    # for i in range(1000):
    #     lst.append(models.UserInfo(username=str(i), password='123'))
    # models.UserInfo.objects.bulk_create(lst)

    """分页器的使用"""
    # user_list = models.UserInfo.objects.all()
    # paginator = Paginator(user_list, 10)
    # print(paginator.count)  # 总共条数
    # print(paginator.num_pages)  # 共几页
    # print(paginator.per_page)  # 一页数量

    # page = paginator.get_page(2)  # 拿到第几页数据
    # print(page.object_list)  # 获取全部数据
    # print(page.has_next())  # 是否有下一页
    # print(page.has_previous())  # 是否有上一页
    # print(page.next_page_number())  # 获取下一页页码
    # print(page.previous_page_number())  # 获取上一页页码

    # page = paginator.get_page(1000)
    # print(page)
    # print(page.object_list)
    # page = paginator.get_page(-1)
    # print(page)
    # print(page.object_list)
    # page = paginator.page(1000)  # EmptyPage
    # print(page)
    # page = paginator.page(-1)  # EmptyPage
    # print(page)

    user_queryset = models.UserInfo.objects.all()
    paginator = Paginator(user_queryset, 10)
    current_page = request.GET.get('page', 1)
    try:
        current_page = int(current_page)
        user_list = paginator.page(current_page)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(1)
    except Exception as e:
        print(e)
        print('server error')
    return render(request, 'paginator/index.html', locals())


def index2(request):
    user_queryset = models.UserInfo.objects.all()
    paginator = Paginator(user_queryset, 10)
    total_pages = paginator.num_pages - 1
    current_page = request.GET.get('page', 1)
    current_page = int(current_page)
    if current_page < 1 or current_page > paginator.num_pages:
        current_page = 1
    previous_page = current_page - 1
    next_page = current_page + 1
    if previous_page == 0:
        page_ranges = range(1, 4)
    elif current_page == paginator.num_pages:
        page_ranges = range(paginator.num_pages - 2, paginator.num_pages + 1)
    else:
        page_ranges = [previous_page, current_page, next_page]
    user_list = paginator.page(current_page)
    return render(request, 'paginator/index2.html', locals())
