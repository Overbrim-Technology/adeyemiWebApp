from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Article, Category


# Create your views here.
def blog(request):
    categories=Category.objects.all()
    blog_posts=Article.objects.all()

    paginated=Paginator(blog_posts, 4)
    page_number= request.GET.get('page')
    page_obj= paginated.get_page(page_number)

    # return render(request,'blog.html')
    return render(request,'blog.html',{'page_obj':page_obj, 'blog_posts':blog_posts, 'categories':categories})