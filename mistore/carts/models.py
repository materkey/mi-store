# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Cart(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='user_cart')
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = u'Корзина'
        verbose_name_plural = u'Корзины'
