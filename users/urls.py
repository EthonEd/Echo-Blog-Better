# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/7/2 17:16
# @Author  :Noperx

from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(), {'LoginView.template_name': 'users/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]


