# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from categories.models import Category
from users.models import User


# from carts.models import Cart

class Product(models.Model):
    active = models.BooleanField(default=True, verbose_name="Показывать")
    product_name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.CharField(max_length=255, default='No description provided')
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    price = models.IntegerField(verbose_name="Цена")
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='products', verbose_name="Категории")
    buyers = models.ManyToManyField(User, related_name='buy_hystory', blank=True)
    def __unicode__(self):
        return self.product_name

    class Meta:
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'
