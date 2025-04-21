from datetime import datetime

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

    return render(request,'blog.html',{'page_obj':page_obj, 'blog_posts':blog_posts, 'categories':categories})

def article(request, category, date_time, slug):
    # article page url will be format adeyemiodubeko.com/{category-datetime}
    try:
        created = datetime.strptime(date_time, '%Y%m%d%H%M%S')
    except ValueError:
        return render(request, '404.html', status=404)

    # article = get_object_or_404(Article, category=category, created=created, slug=slug)
    return render(request, 'blog_article.html', {'article': article})
