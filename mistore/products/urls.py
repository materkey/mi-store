from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required

from views import NewProduct, ProductList, ProductUpdate, ProductDetail, get_product_names, ProductReviews, \
    ProductLikeAjaxView

urlpatterns = [
    url(r'(?P<pk>\d+)/$', ProductDetail.as_view(), name='details'),
    url(r'(?P<pk>\d+)/reviews$', ProductReviews.as_view(), name='reviews'),
    url(r'(?P<pk>\d+)/like$', ProductLikeAjaxView.as_view(), name='like'),
    url(r'(?P<pk>\d+)/edit/$', staff_member_required(ProductUpdate.as_view()), name='edit'),
    url(r'get_product_names/$', get_product_names, name='product_names'),
    url(r'^$', ProductList.as_view(), name='list'),
    url(r'new/$', staff_member_required(NewProduct.as_view()), name='new'),
]
