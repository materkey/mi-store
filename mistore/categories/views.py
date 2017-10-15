# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Category


def view_category(request, pk=None):
    category = get_object_or_404(Category.objects.all(), pk=pk)

    return render(request, 'categories/view_category.html', {'category': category})

class CategoriesList(ListView):
    template_name = 'categories/categories_list.html'
    context_object_name = 'categories'
    model = Category
    # paginate_by = 3
