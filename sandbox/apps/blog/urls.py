# -*- coding: utf-8 -*-
from django.conf.urls import url
# from .views import goview
from .views import (IndexView, DetailView, CategoryView, TagView, AboutView,
                    SilianView, MySearchView, ArchiveView, TimelineView, get_article_detail, DetailModalView)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^hot/$', IndexView.as_view(), {'sort': 'v'}, name='index_hot'),
    url(r'^article/(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),
    url(r'^api/article/(?P<slug>[\w-]+)/$', get_article_detail, name='detailapi'),
    url(r'^article/modal/(?P<slug>[\w-]+)/$', DetailModalView.as_view(), name='detailmodal'),
    url(r'^category/(?P<slug>[\w-]+)/$', CategoryView.as_view(), name='category'),
    url(r'^category/(?P<slug>[\w-]+)/hot/$', CategoryView.as_view(), {'sort': 'v'},
        name='category_hot'),
    url(r'^tag/(?P<slug>[\w-]+)/$', TagView.as_view(), name='tag'),
    url(r'^tag/(?P<slug>[\w-]+)/hot/$', TagView.as_view(), {'sort': 'v'}, name='tag_hot'),
    url(r'^about/$', AboutView, name='about'),  # About页面
    url(r'^timeline/$', TimelineView.as_view(), name='timeline'),
    url(r'archive/$', ArchiveView.as_view(), name='archive'),
    url(r'^silian\.xml$', SilianView.as_view(content_type='application/xml'), name='silian'),
    url(r'^search/$', MySearchView.as_view(), name='search_view'),
]

app_name = 'blog'
