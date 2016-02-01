# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20160201_1429'),
        ('realm', '0001_initial'),
        ('hotel', '0002_auto_20160201_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sold',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auction_id', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('bid', models.PositiveIntegerField()),
                ('buyout', models.PositiveIntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('sold_at', models.DateTimeField(verbose_name=b'now')),
                ('created_at', models.DateTimeField(verbose_name=b'now')),
                ('item', models.ForeignKey(related_name='solds', to='item.Item')),
                ('realm', models.ForeignKey(related_name='solds', to='realm.Realm')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
