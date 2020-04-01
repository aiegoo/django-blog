# Server must be restarted after creating new tags file

from django import template
from ..models import Article, Category, Tag, Carousel, FriendLink
from django.db.models.aggregates import Count
from django.utils.html import mark_safe
import re

register = template.Library ()


# Article-related tag functions
@ register.simple_tag
def get_article_list (sort = None, num = None):
    '' 'Get the specified sorting method and the specified number of articles' ''
    if sort:
        if num:
            return Article.objects.order_by (sort) [: num]
        return Article.objects.order_by (sort)
    if num:
        return Article.objects.all () [: num]
    return Article.objects.all ()


@ register.simple_tag
def keywords_to_str (art):
    '' 'Turn article keywords into strings' ''
    keys = art.keywords.all ()
    return ','. join ([key.name for key in keys])


@ register.simple_tag
def get_tag_list ():
    '' 'Back to tag list' ''
    return Tag.objects.annotate (total_num = Count ('article')). filter (total_num__gt = 0)


@ register.simple_tag
def get_category_list ():
    '' 'Back to category list' ''
    return Category.objects.annotate (total_num = Count ('article')). filter (total_num__gt = 0)


@ register.inclusion_tag ('blog/tags/article_list.html')
def load_article_summary (articles):
    '' 'Back to article list template' ''
    return {'articles': articles}


@ register.inclusion_tag ('blog/tags/pagecut.html', takes_context = True)
def load_pages (context):
    '' 'Paging label template, no need to pass parameters, inherit parameters directly' ''
    return context


# Other functions
@ register.simple_tag
def get_carousel_list ():
    '' 'Get carousel picture list' ''
    return Carousel.objects.all ()


@ register.simple_tag
def get_star (num):
    '' 'Get a row of stars' ''
    tag_i = '<i class = "fa fa-star"> </ i>'
    return mark_safe (tag_i * num)


@ register.simple_tag
def get_star_title (num):
    '' 'Get a description of the number of stars' ''
    the_dict = {
        1: '[1 star]: micro update, involving minor adjustments or planned content later',
        2: '[2 stars]: small updates, small adjustments, tables are generally not migrated',
        3: '[3 stars]: Medium update, generally increase or decrease modules, migration of tables',
        4: '[4 stars]: The big update involves the increase or decrease of applications',
        5: '[5 stars]: Maximum update, generally involving changes in multiple applications and tables',
    }
    return the_dict [num]


@ register.simple_tag
def my_highlight (text, q):
    '' 'Custom title search term highlighting function, ignore case' ''
    if len (q)> 1:
        try:
            text = re.sub (q, lambda a: '<span class = "highlighted"> {} </ span>'. format (a.group ()),
                          text, flags = re.IGNORECASE)
            text = mark_safe (text)
        except:
            pass
    return text


@ register.simple_tag
def get_request_param (request, param, default = None):
    '' 'Get requested parameters' ''
    return request.POST.get (param) or request.GET.get (param, default)


@ register.simple_tag
def get_friends ():
    '' 'Get Active Links' ''
    return FriendLink.objects.filter (is_show = True, is_active = True)