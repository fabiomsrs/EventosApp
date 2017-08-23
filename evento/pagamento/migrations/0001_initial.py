# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inscricao', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.FloatField(null=True)),
                ('pago', models.BooleanField(default=False)),
                ('inscricao', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='meu_pagamento', to='inscricao.Inscricao')),
            ],
        ),
    ]
