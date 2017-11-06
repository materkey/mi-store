# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
