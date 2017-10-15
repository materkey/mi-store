from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required

from views import NewProduct, ProductList, ProductUpdate, ProductDetail

urlpatterns = [
    url(r'(?P<pk>\d+)/$', ProductDetail.as_view(), name='details'),
    url(r'(?P<pk>\d+)/edit/$', staff_member_required(ProductUpdate.as_view()), name='edit'),
    url(r'^$', ProductList.as_view(), name='list'),
    url(r'new/$', staff_member_required(NewProduct.as_view()), name='new'),
]
