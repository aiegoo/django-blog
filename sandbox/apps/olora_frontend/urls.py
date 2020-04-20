from django.conf.urls import url
from .views import Home

urlpatterns = [
    url('^$', Home, name='home'),
]

app_name = 'olora_frontend'
