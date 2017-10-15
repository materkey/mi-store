from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import NewOrder, DeactivateOrderView

urlpatterns = [
    url(r'new/(?P<pk>\d+)$', login_required(NewOrder.as_view()), name='new'),
    url(r'deactivate/(?P<pk>\d+)$', login_required(DeactivateOrderView.as_view()), name='deactivate'),
]
