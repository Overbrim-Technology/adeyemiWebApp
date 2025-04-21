from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_query_name='category')
    # slug = models.SlugField(unique=True, blank=True, null=True)
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

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     timestamp = self.created.strftime('%Y%m%d%H%M%S')
    #     return reverse("article_detail", args=[self.category, timestamp, self.slug])
