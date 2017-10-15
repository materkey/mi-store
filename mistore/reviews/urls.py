from django.conf.urls import url

from views import ReviewUpdate

urlpatterns = [
    url(r'(?P<pk>\d+)/edit$', ReviewUpdate.as_view(), name='edit'),
]
