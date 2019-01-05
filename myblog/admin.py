from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

class CategoriesInline(admin.TabularInline):
	model = Category.post.through
	fields = ('category',)

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'author', 'published_date']
    inlines = [CategoriesInline]

class CategoriesAdmin(admin.ModelAdmin):
	exclude = ['post',]


#admin.site.register(AuthorAdmin)

admin.site.register(Category, CategoriesAdmin)
admin.site.register(Post, PostAdmin)
