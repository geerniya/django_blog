from django.contrib.syndication.views import Feed
from django.urls import reverse

from myblog.models import Blog


class BlogRssFeed(Feed):
    """
    创建一个rss源
    """
    title = "geerniya的博客小屋"
    link = "/rss/"
    def items(self):
        return Blog.objects.all()
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.content
    def item_link(self, item):
        return reverse('blog_id', args=[item.id,])

