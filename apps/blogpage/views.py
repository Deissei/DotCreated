from django.shortcuts import render
from django.views import View
from .models import Blog, Comment
from project.models import Category


class BlogDetailViews(View):
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        blog_all = Blog.objects.all()
        category = Category.objects.all()
        comm = Comment.objects.all()
        context = {
            'blog': blog,
            'blog_all': blog_all,
            'category': category,
            'comm': comm,
        }
        return render(request, 'post1.html', context)