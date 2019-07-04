from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from blog.forms import BlogForm, EntryForm, TopicForm
from blog.models import Blog, Entry, Topic
from blog_django.settings import PAGE_NUM
from comment.forms import CommentForm
from comment.models import Comment


def pages(request, list=Blog.objects.all()):
    paginator = Paginator(list, PAGE_NUM)  # Show 6 blogs per page
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return blogs


def blogs(request):
    # 取全部的博客
    blogs = Blog.objects.all()
    context = {
        'blogs': pages(request, list=blogs)  # 对全部博客进行分页
    }
    return render(request, 'blog/blogs.html', context)


def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    # 上一篇下一篇
    previous_page = Blog.objects.filter(pub_date__gte=blog.pub_date).last() # gte两篇文章同时发表，对于一个用户是不正确的，多用户有很可能
    next_page = Blog.objects.filter(pub_date__lte=blog.pub_date).first()

    # 获取评论对象
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type, object_id=blog.id)

    context = {
        'blog': blog,
        'previous_page': previous_page,
        'next_page': next_page,
        'comments': comments,
        'comment_form': CommentForm(initial={'content_type': blog_content_type.model, 'object_id': blog_id}),

    }
    return render(request, 'blog/blog.html', context)


def new_blog(request):
    """添加新博客"""
    if request.method != 'POST':

        # 未提交数据：创建一个新表单
        form = BlogForm()
    else:
        # POST提交的数据，对数据进行处理
        form = BlogForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.author = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('blog:blogs'))
    context = {'form': form}
    return render(request, 'blog/new_blog.html', context)


def topics(request):
    # 取全部的博客
    topics = Topic.objects.all()
    context = {
        'topics': pages(request, list=topics)  # 对全部博客进行分页
    }
    return render(request, 'blog/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all().order_by('-pub_date')  # 如果为空报错
    context = {
        'topic': topic,
        'entries': pages(request, list=entries),  # 对全部条目进行分页
    }
    return render(request, 'blog/topic.html', context)


def new_topic(request):
    """添加新博客"""
    if request.method != 'POST':

        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.author = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('blog:topics'))
    context = {'form': form}
    return render(request, 'blog/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.author != request.user: raise Http404
    if request.method != 'POST':

        # 未提交数据：创建一个新表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('blog:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'blog/new_entry.html', context)


def edit_entry(request, entry_id):
    """编辑条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.author != request.user: raise Http404
    if request.method != 'POST':

        # 未提交数据：创建一个新表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'blog/edit_entry.html', context)


def all(request):
    return render(request, 'blog/all.html')


def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method != "POST":
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:blog', args=[blog_id]))
    context = {
        'blog': blog,
        'form': form,
    }
    return render(request, 'blog/edit_blog.html', context)
