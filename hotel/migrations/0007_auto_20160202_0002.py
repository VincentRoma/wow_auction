# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_sell_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='item',
            field=models.PositiveIntegerField(null=True),
        ),
    ]