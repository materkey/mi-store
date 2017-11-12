# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    company_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
