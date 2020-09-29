import django
from django.apps import apps
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views
from oscar.views import handler403, handler404, handler500

from apps.gateway import urls as gateway_urls
from apps.sitemaps import base_sitemaps
from apps.olora_frontend import urls as olora_urls
from apps.olora_frontend.views import AutomateDeployment

from django.conf import settings
from django.views.generic import TemplateView

from django.contrib.sitemaps.views import sitemap
from apps.blog.sitemaps import ArticleSitemap, CategorySitemap, TagSitemap
from apps.blog.feeds import AllArticleRssFeed

from rest_framework.routers import DefaultRouter
from apps.api import views as api_views
from apps.olora_frontend.views import contact_us

if settings.API_FLAG:
    router = DefaultRouter()
    router.register(r'users', api_views.UserListSet)
    router.register(r'articles', api_views.ArticleListSet)
    router.register(r'tags', api_views.TagListSet)
    router.register(r'categorys', api_views.CategoryListSet)
    router.register(r'timelines', api_views.TimelineListSet)
    router.register(r'toollinks', api_views.ToolLinkListSet)

# Sitemap
sitemaps = {
    'articles': ArticleSitemap,
    'tags': TagSitemap,
    'categories': CategorySitemap
}

admin.autodiscover()

urlpatterns = [
    url(r'^', include(olora_urls, namespace='olora')),
    url(r'^api/deployment/$', AutomateDeployment, name='automatic_deployment'),
    url('^api/contact_us$', contact_us, name='contact_us'),
    # Include admin as convenience. It's unsupported and only included
    # for developers.
    url(r'^admin/', admin.site.urls),
    # i18n URLS need to live outside of i18n_patterns scope of Oscar
    url(r'^i18n/', include(django.conf.urls.i18n)),

    # include a basic sitemap
    url(r'^sitemap\.xml$', views.index,
        {'sitemaps': base_sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap,
        {'sitemaps': base_sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    ## blog
    url(r'^blog/accounts/', include('allauth.urls')),  # allauth
    url(r'^blog/accounts/', include('apps.oauth.urls', namespace='oauth')),
    url('^blog/', include('apps.blog.urls', namespace='blog')),  # blog
    url(r'^blog/comment/', include('apps.comment.urls', namespace='comment')),  # comment
    url(r'^blog/robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^blog/sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^blog/feed/$', AllArticleRssFeed(), name='rss'),  # rss订阅
    url(r'mdeditor/', include('mdeditor.urls'))
]

# Prefix Oscar URLs with language codes
urlpatterns += i18n_patterns(
    #url(r'^', include(olora_urls, namespace='olora')),
    # Custom functionality to allow dashboard users to be created
    url(r'gateway/', include(gateway_urls)),
    # Oscar's normal URLs
    url(r'oscar/', include(apps.get_app_config('oscar').urls[0])),
)

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
                   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        url(r'^403$', handler403, {'exception': Exception()}),
        url(r'^404$', handler404, {'exception': Exception()}),
        url(r'^500$', handler500),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

if settings.API_FLAG:
    urlpatterns.append(url(r'^api/v1/', include(router.urls)))  # restframework

if settings.TOOL_FLAG:
    urlpatterns.append(url(r'^blog/tool/', include('apps.tool.urls', namespace='tool')))  # tool
