from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
