from django.contrib.syndication.views import Feed
from .models import Article
from django.conf import settings

class AllArticleRssFeed (Feed):
    # Title displayed on party reader
    title = settings.SITE_END_TITLE
    # Jump URL for homepage
    link = "/"
    # Description
    description = settings.SITE_DESCRIPTION
    # Content items to be displayed, this can pick some popular or latest blogs by yourself
    def items (self):
        return Article.objects.all () [: 100]

    # Title of the displayed content, this is the main thing
    def item_title (self, item):
        return "[{}] {}". format (item.category, item.title)

    # Description of displayed content
    def item_description (self, item):
        return item.body_to_markdown ()