# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20160201_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(null=True, verbose_name=b'now'),
        ),
    ]