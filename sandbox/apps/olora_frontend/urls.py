from django.conf.urls import url
from .views import Home, home_en, home_kn

urlpatterns = [
    url('^en/$', home_en, name='homeen'),
    url('^kn/$', home_kn, name='homekn'),
    url('^$', Home, name='home'),
]

app_name = 'olora_frontend'
