# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/7/3 11:16
# @Author  :Noperx
from ckeditor.widgets import CKEditorWidget
from django import forms
from mdeditor.widgets import MDEditorWidget

from blog.models import Blog, Entry, Topic


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['author']
        labels = {'title': '标题', 'tag': '标签', 'content': '正文'}
        widgets = {
            # 'content': CKEditorWidget(config_name='comment_custom'),
            'content': CKEditorWidget(),
        }


class TopicForm(forms.ModelForm):
    class Meta:
        # model = Blog 没改过来。。。。。。。。。。。。。。。。。。。。。
        model = Topic
        exclude = ['author']
        labels = {'name': '标题', 'tag': '标签', 'tagline': '简介'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ['pub_date', 'mod_date', 'blog']
        labels = {'headline': '标题', 'body_text': '正文'}
        widgets = {
            'body_text': CKEditorWidget(),
            # 'body_text': CKEditorWidget(config_name='comment_custom'),
            # 'body_text': CKEditorWidget(),
        }