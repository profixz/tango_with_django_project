# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-05 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_remove_page_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='page',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
