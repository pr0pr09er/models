from django.shortcuts import render, HttpResponse
from postApp import forms
from .models import Post


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'all.html', {'posts': posts})


def add_new(request):
    if request.method == 'POST':
        header = request.POST.get('header')
        content = request.POST.get('content')
        is_publish = request.POST.get('is_publish')
        date = request.POST.get('date')
        if is_publish == 'on':
            is_publish = True
        else:
            is_publish = False
        post = Post.objects.create(header=header, content=content, is_publish=is_publish, date=date)
        post.save()
        return HttpResponse('<h2>Post published</h2>')
    else:
        post = forms.PostForm()
        return render(request, 'add_new.html', {'form': post})
