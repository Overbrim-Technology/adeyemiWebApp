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
    body = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.title
