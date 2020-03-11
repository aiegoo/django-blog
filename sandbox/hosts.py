from django.conf import settings
from django_hosts import patterns, host
import urls

host_patterns = patterns(
    '',
    host(r'latest', urls, name='latest'),
)