# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from products.models import Product
from reviews.models import Review

def get_main(request):

    products = Product.objects.all()[:5]
    reviews = Review.objects.all()[:5]

    return render(request, 'main/main.html', {'products' : products, 'reviews' : reviews})
