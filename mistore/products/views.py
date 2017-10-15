# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from reviews.models import Review
from .models import Product


class ProductDetail(CreateView):
    model = Review
    template_name = 'products/product_details.html'
    fields = ('text',)

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.productobject = get_object_or_404(Product, id=pk)
        return super(ProductDetail, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.reviewed_product = self.productobject
        return super(ProductDetail, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['product'] = self.productobject
        return context

    def get_success_url(self):
        return reverse('products:details', kwargs={'pk': self.productobject.pk})


class ProductsListForm(forms.Form):
    order_by = forms.ChoiceField(label='Упорядочить', choices=(
        ('product_name', 'По алфавиту'),
        ('-product_name', 'В обратном порядке'),
        ('id', 'По коду товара'),
    ), required=False)
    search = forms.CharField(label='Поиск', required=False)
    price_gt = forms.IntegerField(label='Цена от', required=False)
    price_lt = forms.IntegerField(label='Цена до', required=False)


class ProductList(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    model = Product
    paginate_by = 3

    def get_queryset(self):
        p = super(ProductList, self).get_queryset().filter(active='True')

        self.form = ProductsListForm(self.request.GET)

        if self.form.is_valid():
            if self.form.cleaned_data['price_gt']:
                p = p.filter(price__gt=self.form.cleaned_data['price_gt'])
            if self.form.cleaned_data['price_lt']:
                p = p.filter(price__lt=self.form.cleaned_data['price_lt'])
            if self.form.cleaned_data['order_by']:
                p = p.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                p = p.filter(product_name__icontains=self.form.cleaned_data['search'])

        return p

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['searchform'] = self.form
        return context


class NewProduct(CreateView):
    template_name = 'products/new_product.html'
    model = Product
    fields = 'product_name', 'price', 'categories'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewProduct, self).form_valid(form)

    def get_success_url(self):
        return reverse('products:details', kwargs={'pk': self.object.pk})


class ProductUpdate(UpdateView):
    template_name = 'products/edit_product.html'
    model = Product
    fields = 'product_name', 'price', 'categories', 'active',

    def get_queryset(self):
        return super(ProductUpdate, self).get_queryset().filter(
            author=self.request.user)  # вроде ограничивать по автору создание товара в будущем не понадобится

    def get_success_url(self):
        return reverse('products:details', kwargs={'pk': self.object.pk})
