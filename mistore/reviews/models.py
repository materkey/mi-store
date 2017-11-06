# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from products.models import Product


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews')
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    reviewed_product = models.ForeignKey(Product, related_name='reviews')

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = u'Отзыв'
        verbose_name_plural = u'Отзывы'