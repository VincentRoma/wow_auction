# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='auction_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='bid',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='buyout',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sells', to='item.Item'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='owner',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='sell',
            name='realm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sells', to='realm.Realm'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='timeLeft',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
