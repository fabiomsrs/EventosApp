# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 03:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos_app', '0004_auto_20170722_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='valorTotal',
            field=models.FloatField(default=0),
        ),
    ]
