# -*- coding: utf-8 -*-
from django import template
from django.db.models.aggregates import Count
from ..models import ToolCategory,ToolLink

register = template.Library()

@register.simple_tag
def get_toolcates():
    '''Get all tool categories, only show the categories with tools'''
    return ToolCategory.objects.annotate(total_num=Count('toollink')).filter(total_num__gt=0)

@register.simple_tag
def get_toollinks(cate):
    '''Get all tools in a single category'''
    return cate.toollink_set.all()
