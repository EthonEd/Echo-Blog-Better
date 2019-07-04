# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/7/2 16:19
# @Author  :Noperx
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')