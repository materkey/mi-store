# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Product


def product_detail(request, pk=None):
    product = get_object_or_404(Product.objects.all(), pk=pk)
    return render(request, 'products/product_details.html', {'product' : product})

