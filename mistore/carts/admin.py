# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cart
from orders.models import Order

class OrderInlineAdmin(admin.TabularInline):
    model = Order

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [OrderInlineAdmin]
