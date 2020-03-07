# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-17 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0027_auto_20200217_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='depositdeduct',
            name='deduct_type',
            field=models.SmallIntegerField(choices=[(1, '逾期扣款'), (2, '支付抵扣')], default=1, verbose_name='扣款类型'),
        ),
        migrations.AlterField(
            model_name='depositdeduct',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='金额'),
        ),
        migrations.AlterField(
            model_name='discountsrecord',
            name='dis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.Discounts', verbose_name='优惠卷'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_type',
            field=models.PositiveSmallIntegerField(choices=[(1, '未支付'), (2, '待收货'), (3, '已完成'), (4, '逾期未支付')], default=2, verbose_name='支付状态'),
        ),
    ]
