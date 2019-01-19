from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.models import Post

class PostFeed(Feed):
    title = 'Latest posts from the blog'
    link = '/latest/feed'
    description = 'Latest blog posts'
    def items(self):
        return Post.objects.order_by('-published_date')[:5]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.text

 


