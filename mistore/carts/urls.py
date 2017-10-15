from django.conf.urls import url

from carts.views import CartList, checkout

urlpatterns = [
    url(r'^$', CartList.as_view(), name='list'),
    url(r'checkout$', checkout, name='checkout'),
]
