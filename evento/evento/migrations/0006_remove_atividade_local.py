# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0005_atividade_local'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='local',
        ),
    ]
