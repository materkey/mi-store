# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171016_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='buy_hystory',
        ),
    ]
