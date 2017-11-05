from django.conf.urls import url
from views import user_detail, cabinet

urlpatterns = [
    url(r'detail/(?P<pk>\d+)/$', user_detail),
    url(r'cabinet/(?P<pk>\d+)/$', cabinet),
]