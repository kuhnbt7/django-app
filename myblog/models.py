from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return '/posts/{}'.format(self.id)

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    post = models.ManyToManyField(Post, blank=True, related_name='categories')
    
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
