from django.conf.urls import url

from views import get_main

urlpatterns = [
    url(r'^', get_main, name="main_page"),
]