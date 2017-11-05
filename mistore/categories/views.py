# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Category

def view_category(request, pk=None):

    category = get_object_or_404(Category.objects.all(), pk=pk)
    
    return render(request, 'categories/view_category.html', {'category' : category})
