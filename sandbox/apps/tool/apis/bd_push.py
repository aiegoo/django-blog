import requests
import re

def push_urls(url, urls):
    '''Push the link according to the API provided by the Baidu webmaster'''
    headers = {
        'User-Agent': 'curl/7.12.1',
        'Host': 'data.zz.baidu.com',
        'Content - Type': 'text/plain',
        'Content - Length': '83'
    }
    try:
        html = requests.post(url, headers=headers, data=urls, timeout=5).text
        return html
    except:
        return "{'error':404,'message':'Request timed out, interface address is wrong!'}"

def get_urls(url):
    '''Extract all links in the sitemap. The parameter must be a link to the sitemap.'''
    try:
        html = requests.get(url,timeout=5).text
    except:
        return 'miss'
    else:
        urls = re.findall('<loc>\s*?(.*?)\s*?</loc>', html)
        return '\n'.join(urls)


if __name__ == '__main__':
    url = 'www.stopfollow-sh_8i.com'
    u = re.findall(r'(http|https://.*?)/.*?', url)
    home_url = u[0] if u else url
    print(home_url)