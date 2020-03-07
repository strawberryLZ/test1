# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-13 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0019_auto_20200213_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deposit_price',
            field=models.PositiveIntegerField(null=True, verbose_name='使用保证金金额'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, '未支付'), (2, '待收货'), (3, '已完成'), (4, '逾期未支付')], verbose_name='状态'),
        ),
    ]
