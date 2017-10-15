# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from mistore import settings
from products.models import Product


class ProductLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    product = models.ForeignKey(Product, related_name='likes')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def active_set(self):
        return

    # product_name = models.CharField(max_length=255)
    # description = models.CharField(max_length=255, default='No description provided')
    # photo = models.ImageField(upload_to='photos', blank=True, null=True)
    # price = models.IntegerField()
    #

    # categories = models.ManyToManyField(Category, related_name='products')
    # buyers = models.ManyToManyField(User, related_name='buy_hystory')
    #
    # def __unicode__(self):
    #     return self.product_name
    #
    # class Meta:
    #     verbose_name = u'Товар'
    #     verbose_name_plural = u'Товары'
