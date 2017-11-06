from django.conf.urls import url
from views import user_details, cabinet

urlpatterns = [
    url(r'details/(?P<pk>\d+)/$', user_details, name='details'),
    url(r'cabinet/$', cabinet, name='cabinet'),
]