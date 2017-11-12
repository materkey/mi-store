from django.conf.urls import url
from django.contrib.auth.views import login, logout

from views import user_details, cabinet, CreateUser

urlpatterns = [
    url(r'details/(?P<pk>\d+)/$', user_details, name='details'),
    url(r'profile/$', cabinet, name='cabinet'),
    url(r'login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'logout/$', logout, {'next_page': 'main:main'}, name='logout'),
    url('^register/$', CreateUser.as_view(), name='register'),
    # url(r'register/$', CreateUser.as_view, name='register'),
]
