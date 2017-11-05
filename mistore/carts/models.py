# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_cart')

    class Meta:
        verbose_name = u'Корзина'
        verbose_name_plural = u'Корзины'