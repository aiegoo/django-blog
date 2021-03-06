import datetime
import time

import markdown
from django.conf import settings
from django.core.cache import cache
from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify
from django.views import generic
from haystack.generic_views import SearchView  # Import search view
from haystack.query import SearchQuerySet
from markdown.extensions.toc import TocExtension  # Anchor extension
from rest_framework.decorators import renderer_classes, api_view
import json
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import Article, Tag, Category, Timeline, Silian


# Create your views here.

class ArchiveView(generic.ListView):
    model = Article
    template_name = 'blog/archive.html'
    context_object_name = 'articles'
    paginate_by = 200
    paginate_orphans = 50


class IndexView(generic.ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = getattr(settings, 'BASE_PAGE_BY', None)
    paginate_orphans = getattr(settings, 'BASE_ORPHANS', 0)

    def get_ordering(self):
        ordering = super(IndexView, self).get_ordering()
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return ('-views', '-update_date', '-id')
        return ordering


class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get_object(self):
        obj = super(DetailView, self).get_object()
        # Set the increase of page views to determine the time. If the same article is viewed more than half an hour
        # twice, the page views will be re-counted. The author will ignore the view.
        u = self.request.user
        ses = self.request.session
        the_key = 'is_read_{}'.format(obj.id)
        is_read_time = ses.get(the_key)
        if u != obj.author:
            if not is_read_time:
                obj.update_views()
                ses[the_key] = time.time()
            else:
                now_time = time.time()
                t = now_time - is_read_time
                if t > 60 * 30:
                    obj.update_views()
                    ses[the_key] = time.time()
        # Get the update time of the article and determine whether to take the markdown of the article from the cache, which can avoid conversion every time
        ud = obj.update_date.strftime("%Y%m%d%H%M%S")
        md_key = '{}_md_{}'.format(obj.id, ud)
        cache_md = cache.get(md_key)
        if cache_md:
            md = cache_md
        else:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                TocExtension(slugify=slugify),
            ])
            cache.set(md_key, md, 60 * 60 * 12)
        obj.body = md.convert(obj.body)
        obj.toc = md.toc
        return obj


class DetailModalView(generic.DetailView):
    model = Article
    template_name = 'blog/detailmodal.html'
    context_object_name = 'article'

    def get_object(self):
        obj = super(DetailModalView, self).get_object()
        # Set the increase of page views to determine the time. If the same article is viewed more than half an hour
        # twice, the page views will be re-counted. The author will ignore the view.
        u = self.request.user
        ses = self.request.session
        the_key = 'is_read_{}'.format(obj.id)
        is_read_time = ses.get(the_key)
        if u != obj.author:
            if not is_read_time:
                obj.update_views()
                ses[the_key] = time.time()
            else:
                now_time = time.time()
                t = now_time - is_read_time
                if t > 60 * 30:
                    obj.update_views()
                    ses[the_key] = time.time()
        # Get the update time of the article and determine whether to take the markdown of the article from the cache, which can avoid conversion every time
        ud = obj.update_date.strftime("%Y%m%d%H%M%S")
        md_key = '{}_md_{}'.format(obj.id, ud)
        cache_md = cache.get(md_key)
        if cache_md:
            md = cache_md
        else:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                TocExtension(slugify=slugify),
            ])
            cache.set(md_key, md, 60 * 60 * 12)
        obj.body = md.convert(obj.body)
        obj.toc = md.toc
        return obj


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_article_detail(request, slug, format=None):
    obj = Article.objects.get(slug=slug)
    # Set the increase of page views to determine the time. If the same article is viewed more than half an hour
    # twice, the page views will be re-counted. The author will ignore the view.
    u = request.user
    ses = request.session
    the_key = 'is_read_{}'.format(obj.id)
    is_read_time = ses.get(the_key)
    if u != obj.author:
        if not is_read_time:
            obj.update_views()
            ses[the_key] = time.time()
        else:
            now_time = time.time()
            t = now_time - is_read_time
            if t > 60 * 30:
                obj.update_views()
                ses[the_key] = time.time()
    # Get the update time of the article and determine whether to take the markdown of the article from the
    # cache, which can avoid conversion every time
    ud = obj.update_date.strftime("%Y%m%d%H%M%S")
    md_key = '{}_md_{}'.format(obj.id, ud)
    cache_md = cache.get(md_key)
    if cache_md:
        md = cache_md
    else:
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        cache.set(md_key, md, 60 * 60 * 12)
    obj.body = md.convert(obj.body)
    obj.toc = md.toc
    article = {
        'title': obj.title,
        'body': obj.body,
    }
    return Response(article)


class CategoryView(generic.ListView):
    model = Article
    template_name = 'blog/category.html'
    context_object_name = 'articles'
    paginate_by = getattr(settings, 'BASE_PAGE_BY', None)
    paginate_orphans = getattr(settings, 'BASE_ORPHANS', 0)

    def get_ordering(self):
        ordering = super(CategoryView, self).get_ordering()
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return '-views', '-update_date', '-id'
        return ordering

    def get_queryset(self, **kwargs):
        queryset = super(CategoryView, self).get_queryset()
        cate = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return queryset.filter(category=cate)

    def get_context_data(self, **kwargs):
        context_data = super(CategoryView, self).get_context_data()
        cate = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        context_data['search_tag'] = 'Article Category'
        context_data['search_instance'] = cate
        return context_data


class TagView(generic.ListView):
    model = Article
    template_name = 'blog/tag.html'
    context_object_name = 'articles'
    paginate_by = getattr(settings, 'BASE_PAGE_BY', None)
    paginate_orphans = getattr(settings, 'BASE_ORPHANS', 0)

    def get_ordering(self):
        ordering = super(TagView, self).get_ordering()
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return ('-views', '-update_date', '-id')
        return ordering

    def get_queryset(self, **kwargs):
        queryset = super(TagView, self).get_queryset()
        tag = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        return queryset.filter(tags=tag)

    def get_context_data(self, **kwargs):
        context_data = super(TagView, self).get_context_data()
        tag = get_object_or_404(Tag, slug=self.kwargs.get('slug'))
        context_data['search_tag'] = 'Article tags'
        context_data['search_instance'] = tag
        return context_data


def AboutView(request):
    site_date = datetime.datetime.strptime('2018-04-12', '%Y-%m-%d')
    return render(request, 'blog/about.html', context={'site_date': site_date})


class TimelineView(generic.ListView):
    model = Timeline
    template_name = 'blog/timeline.html'
    context_object_name = 'timeline_list'


class SilianView(generic.ListView):
    model = Silian
    template_name = 'blog/silian.xml'
    context_object_name = 'badurls'


# Rewrite the search view, you can add some additional parameters, and you can redefine the name
class MySearchView(SearchView):
    context_object_name = 'search_list'
    paginate_by = getattr(settings, 'BASE_PAGE_BY', None)
    paginate_orphans = getattr(settings, 'BASE_ORPHANS', 0)
    queryset = SearchQuerySet().order_by('-views')
