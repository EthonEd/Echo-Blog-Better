# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/7/4 11:11
# @Author  :Noperx
from django.urls import path

from . import views

app_name = 'comment'
urlpatterns = [
    path('update_comment/', views.update_comment, name='update_comment'),
]