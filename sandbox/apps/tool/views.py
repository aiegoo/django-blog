from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.utils.html import mark_safe
from .apis.bd_push import push_urls, get_urls
from .apis.links_test import Check
from .apis.useragent import get_user_agent

import re
import markdown


# Create your views here.

def Toolview(request):
    return render(request, 'tool/tool.html')


# Baidu Active Push
def BD_pushview(request):
    return render(request, 'tool/bd_push.html')


@require_POST
def bd_api_view(request):
    if request.is_ajax():
        data = request.POST
        url = data.get('url')
        urls = data.get('url_list')
        info = push_urls(url, urls)
        return JsonResponse({'msg': info})
    return JsonResponse({'msg': 'miss'})


# Baidu proactively upgrades, extracting sitemap links
def BD_pushview_site(request):
    return render(request, 'tool/bd_push_site.html')


@require_POST
def bd_api_site(request):
    if request.is_ajax():
        data = request.POST
        url = data.get('url')
        map_url = data.get('map_url')
        urls = get_urls(map_url)
        if urls == 'miss':
            info = "{'error':404,'message':'sitemap address request timed out, please check the link address!'}"
        elif urls == '':
            info = "{'error':400,'message':'The sitemap page does not extract valid links, and the sitemap format is not standardized.'}"
        else:
            info = push_urls(url, urls)
        return JsonResponse({'msg': info})
    return JsonResponse({'msg': 'miss'})


# Friendly chain detection
def Link_testview(request):
    return render(request, 'tool/link_test.html')


@require_POST
def Link_test_api(request):
    if request.is_ajax():
        data = request.POST
        p = data.get('p')
        urls = data.get('urls')
        c = Check(urls, p)
        info = c.run()
        return JsonResponse(info)
    return JsonResponse({'msg': 'miss'})


# Online regular expression
def regexview(request):
    return render(request, 'tool/regex.html')


@require_POST
def regex_api(request):
    if request.is_ajax():
        data = request.POST
        texts = data.get('texts')
        regex = data.get('r')
        try:
            lis = re.findall(r'{}'.format(regex), texts)
        except:
            lis = []
        num = len(lis)
        info = '\n'.join(lis)
        result = "Match{}Results:\n".format(num) + "```\n" + info + "\n```"
        result = markdown.markdown(result, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        return JsonResponse({'result': mark_safe(result), 'num': num})
    return JsonResponse({'msg': 'miss'})


# Generate request header
def useragent_view(request):
    return render(request, 'tool/useragent.html')


@require_POST
def useragent_api(request):
    if request.is_ajax():
        data = request.POST
        d_lis = data.get('d_lis')
        os_lis = data.get('os_lis')
        n_lis = data.get('n_lis')
        d = d_lis.split(',') if len(d_lis) > 0 else None
        os = os_lis.split(',') if len(os_lis) > 0 else None
        n = n_lis.split(',') if len(n_lis) > 0 else None
        result = get_user_agent(os=os, navigator=n, device_type=d)
        return JsonResponse({'result': result})
    return JsonResponse({'msg': 'miss'})


# HTML special character comparison table
def html_characters(request):
    return render(request, 'tool/characters.html')