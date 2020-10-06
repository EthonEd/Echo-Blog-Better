# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/7/2 16:19
# @Author  :Noperx
import datetime

from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone

from blog.models import Blog
from read_statistics.utils import week_statistic_data, read_hot_today


def home(request):
    context = common(request)
    return render(request, 'home.html', context)


def read_hot_week():
    today = timezone.now().date()
    seven_days_ago = today - datetime.timedelta(days=7)
    blogs = Blog.objects.filter(read_details__date__lt=today, read_details__date__gte=seven_days_ago) \
        .values('id', 'title') \
        .annotate(read_num_sum=Sum('read_details__read_num')) \
        .order_by('-read_num_sum')
    return blogs[:3]


def common(request):

    # 统计按年月分的博客数
    blog_date_list = Blog.objects.dates('pub_date', 'month', order='DESC')
    blog_date_dict = {}
    for blog_date in blog_date_list:
        blog_date_dict[blog_date] = Blog.objects. \
            filter(pub_date__year=blog_date.year, pub_date__month=blog_date.month).count()

    # 统计一周的博文访问量
    content_type = ContentType.objects.get_for_model(Blog)
    read_nums, dates = week_statistic_data(content_type)  # 一周数据

    # 设置缓存
    read_hot_week_blogs = cache.get("read_hot_week_blogs")
    if read_hot_week_blogs is None:
        read_hot_week_blogs = read_hot_week()
        cache.set('read_hot_week_blogs', read_hot_week(), 60)
    else:
        print('use cache')

    context = {
        'blog_date_dict': blog_date_dict,
        'read_nums': read_nums,  # 一周数据
        'dates': dates,  # 对应日期
        'read_hot_today_datas': read_hot_today(content_type),
        'read_hot_week_blogs': read_hot_week_blogs,
    }
    return context