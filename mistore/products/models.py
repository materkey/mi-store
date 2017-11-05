# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from categories.models import Category
#from carts.models import Cart

class Product(models.Model):
    active = models.BooleanField(default=True)
    product_name = models.CharField(max_length=255, default='Xiaomi Device')
    description = models.CharField(max_length=255, default='No description provided')
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    price = models.IntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='products')
    #carts = models.ManyToManyField(Cart, related_name='products')

    def __unicode__(self):
        return self.product_name

    class Meta:
        #ordering = '-id'
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'
