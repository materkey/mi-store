# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from products.models import Product
from carts.models import Cart


class Order(models.Model):
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, related_name='orders')
    cart = models.ForeignKey(Cart, related_name='customer_orders')

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'