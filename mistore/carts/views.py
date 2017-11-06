# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Cart


def get_cart(request, pk=None):

    cart = get_object_or_404(Cart.objects.all(), pk=pk)

    return render(request, 'carts/get_cart.html', {'cart' : cart})