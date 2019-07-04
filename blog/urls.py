# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/7/2 15:21
# @Author  :Noperx
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:page>/', views.blogs, name='blogs'),  # 这要强转为int，否则报错未知未知参数page
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),

    path('tp/', views.topics, name='topics'),  # 这要必须写个空page，让初始匹配
    path('tp/<int:page>/', views.topics, name='topics'),  # 这要强转为int，否则报错未知未知参数paged
    path('tipics/<int:topic_id>/', views.topic, name='topic'),
    path('topics/<int:topic_id>/<int:page>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    path('all/', views.all, name='all'),
]

# 修改没问题时报错，注意浏览器缓存问题
