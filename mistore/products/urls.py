from django.conf.urls import url
from views import product_details

urlpatterns = [
    url(r'(?P<pk>\d+)/$', product_details, name='details'),
]