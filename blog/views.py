from django.shortcuts import render

from .models import Article, Category


# Create your views here.
def blog(request):
    categories=Category.objects.all
    blog_posts=Article.objects.all

    # return render(request,'blog.html')
    return render(request,'blog.html',{'blog_posts':blog_posts, 'categories':categories})