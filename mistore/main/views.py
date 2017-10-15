# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from products.models import Product
from reviews.models import Review


def get_main(request):
    products = Product.objects.filter(active='True').order_by('-created_at')[:5]
    reviews = Review.objects.filter(deleted='False').order_by('-created_at')[:5]

    return render(request, 'main/main.html', {'products': products, 'reviews': reviews})
