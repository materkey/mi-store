from django.conf.urls import url

from views import view_category, CategoriesList

urlpatterns = [
    url(r'(?P<pk>\d+)/$', view_category, name='view'),
    url(r'^$', CategoriesList.as_view(), name='list'),
]
