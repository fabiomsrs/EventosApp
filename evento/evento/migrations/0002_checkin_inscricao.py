# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-25 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0001_initial'),
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='inscricao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inscricao.RelacionamentoAtividadeInscricao'),
        ),
    ]
