# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from products.models import Product

class ReviewQuerySet(models.QuerySet):

    def available_for_users(self, user):
        return self.filter(models.Q(author=user) | models.Q(deleted=False))


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews')
    text = models.CharField(max_length=255, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False, verbose_name='Удалить')
    reviewed_product = models.ForeignKey(Product, related_name='reviews')

    objects = ReviewQuerySet.as_manager()

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = u'Отзыв'
        verbose_name_plural = u'Отзывы'
