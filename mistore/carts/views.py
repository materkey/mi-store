# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from orders.models import Order


class CartList(ListView):
    template_name = 'carts/cart_list.html'
    context_object_name = 'orders'
    model = Order

    # paginate_by = 3

    def get_queryset(self):
        p = super(CartList, self).get_queryset().filter(cart__customer=self.request.user, cart__active=True)

        return p

def checkout(request):
    user = request.user
    # cart = get_object_or_404(Cart, )

    return render(request, 'carts/checkout.html', {'user': user})