# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-12 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0009_auto_20200212_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailcommoditypic',
            name='key',
        ),
    ]
