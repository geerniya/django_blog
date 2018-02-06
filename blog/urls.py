"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from myblog.views import IndexView, ArichiveView, TagView, TagDetailView, BlogDetailView
from myblog.views import AddCommentView, CategoryDetaiView, MySearchView
from myblog.feeds import BlogRssFeed
from blog.settings import STATIC_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^archive/$', ArichiveView.as_view(), name='archive'),
    url(r'^tags/$', TagView.as_view(), name='tags'),
    url(r'^tags/(?P<tag_name>\w+)$', TagDetailView.as_view(), name='tag_name'),
    url(r'^blog/(?P<blog_id>\d+)$', BlogDetailView.as_view(), name='blog_id'),
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    url(r'^rss/$', BlogRssFeed(), name='rss'),
    url(r'^category/(?P<category_name>\w+)/$', CategoryDetaiView.as_view(), name='category_name'),
    url(r'^search/', MySearchView(),  name='haystack_search'),
    #添加静态文件的访问处理函数
    url(r'^static/(?P<path>.*)/$', serve, {'document_root': STATIC_ROOT}),

]


# 配置全局404页面
hander404 = 'myblog.views.page_not_found'

# 配置全局505页面
hander505 = 'myblog.views.page_errors'
