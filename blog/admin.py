from django.contrib import admin

from blog.models import Blog, Entry, Topic, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'tag', 'pub_date', 'author']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tagline', 'tag', 'pub_date', 'author']


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['headline', 'body_text', 'pub_date']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag_name']
