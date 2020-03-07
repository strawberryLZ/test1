# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-13 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0012_auto_20200213_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionpayment',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, '竞价'), (2, '成交'), (3, '逾期未付款')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='auctionpayment',
            name='auction_price',
            field=models.IntegerField(verbose_name='出价'),
        ),
    ]
