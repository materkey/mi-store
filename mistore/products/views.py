# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django import forms
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from likes.models import ProductLike
from reviews.models import Review
from .models import Product


class ProductDetail(CreateView):
    model = Review
    template_name = 'products/product_details.html'
    fields = ('text',)

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.productobject = get_object_or_404(Product, id=pk)
        self.user = request.user
        return super(ProductDetail, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.reviewed_product = self.productobject
        return super(ProductDetail, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['product'] = self.productobject
        context['reviews'] = self.productobject.reviews.all()
        return context

    def get_success_url(self):
        return reverse('products:details', kwargs={'pk': self.productobject.pk})

class ProductReviews(DetailView):
    model = Product
    template_name = 'products/product_reviews.html'
    context_object_name = 'product'

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.productobject = get_object_or_404(Product, id=pk)
        self.user = request.user
        return super(ProductReviews, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductReviews, self).get_context_data(**kwargs)
        context['reviews'] = self.productobject.reviews.available_for_users(self.user)
        return context

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
        )  # author=self.request.user)  # вроде ограничивать по автору создание товара в будущем не понадобится

    def get_success_url(self):
        if (self.object.active == True):
            return reverse('products:details', kwargs={'pk': self.object.pk})
        else:
            return reverse_lazy('main:main')


def get_product_names(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(active='True').filter(product_name__icontains=q)
        results = []
        for pr in products:
            product_json = {}
            product_json = pr.product_name
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = "fail"
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

class ProductLikeAjaxView(View):

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.product_object = get_object_or_404(Product, id=pk)
        if not request.user.is_authenticated():
            return HttpResponse(ProductLike.objects.filter(product=self.product_object, active=True).count())
        return super(ProductLikeAjaxView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse(ProductLike.objects.filter(product=self.product_object, active=True).count())

    def post(self, request):
        if not self.product_object.likes.filter(user=self.request.user).exists():
            like = ProductLike.objects.create(user=self.request.user, product=self.product_object);
            like.save()
        else:
            like = ProductLike.objects.get(user=self.request.user, product=self.product_object);
            like.active = not like.active
            like.save()
        return HttpResponse(ProductLike.objects.filter(product=self.product_object, active=True).count())