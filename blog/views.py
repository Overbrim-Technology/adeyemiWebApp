from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Article, Category

# Create your views here.
def blog(request):
    categories=Category.objects.all()
    articles=Article.objects.all().order_by('-created')

    paginated=Paginator(articles, 4)
    page_number= request.GET.get('page')
    page_obj= paginated.get_page(page_number)

    return render(request,'blog.html',{'page_obj':page_obj, 'articles':articles, 'categories':categories})

def article(request, slug):
    # article page url will be format adeyemiodubeko.com/{category-datetime}
    # try:
    #     created = datetime.strptime(datetime, '%Y%m%d%H%M%S')
    #     print(created)
    # except ValueError:
    #     return render(request, '404.html', status=404)

    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog_article.html', {'article': article})
