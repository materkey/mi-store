from django.conf.urls import url
from views import product_detail

urlpatterns = [
    url(r'(?P<pk>\d+)/$', product_detail, name='detail'),
]