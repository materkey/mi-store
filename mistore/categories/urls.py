from django.conf.urls import url

from views import view_category

urlpatterns = [
    url(r'(?P<pk>\d+)/$', view_category, name='view'),
]
