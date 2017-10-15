# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView

from carts.models import Cart
from orders.models import Order
from products.models import Product


class NewOrder(CreateView):
    template_name = 'orders/new_order.html'
    model = Order
    fields = 'quantity',

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.productobject = get_object_or_404(Product, id=pk)
        self.user = request.user
        return super(NewOrder, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.product = self.productobject
        form.instance.price = self.productobject.price
        form.instance.cart, created = Cart.objects.get_or_create(customer=self.user)  # , active=True)

        return super(NewOrder, self).form_valid(form)

    def get_success_url(self):
        return reverse('products:details', kwargs={'pk': self.object.product.pk})

class DeactivateOrderView(View):

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.order = get_object_or_404(Order, id=pk)
        return super(DeactivateOrderView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        self.order.active = False
        self.order.save()
        return HttpResponse("OK")

