from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_query_name='category')
    slug = models.SlugField(unique=True, blank=False, null=False)
    description = models.TextField()
    body = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         timestamp = self.created.strftime('%Y%m%d%H%M%S') if self.created else ''
    #         self.slug = slugify(f"{self.title}-{timestamp}")
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("article", args=[self.slug])

# from blog.models import Article
# from django.utils.text import slugify

# for article in Article.objects.all():
#     base_slug=slugify(f"{article.title}-{article.created.strftime('%Y%m%d%H%M%S')}-{article.category}")
#     slug = base_slug
#     counter = 1
#     while Article.objects.filter(slug=slug).exclude(id=article.id).exists():
#         slug = f"{base_slug}-{counter}"
#         counter+=1
#     article.slug = slug
#     article.save()