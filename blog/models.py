from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=20)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)  # models.DateField 没有小时和分钟
    mod_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class Topic(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    tag = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pub_date']


# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)
    # n_comments = models.IntegerField()
    # n_pingbacks = models.IntegerField()
    # rating = models.IntegerField()

    def __str__(self):
        return self.headline

