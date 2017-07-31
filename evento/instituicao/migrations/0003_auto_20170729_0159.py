# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 04:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import instituicao.models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0004_auto_20170729_0158'),
        ('instituicao', '0002_auto_20170727_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Associacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_associacao', enumfields.fields.EnumField(default='default', enum=instituicao.models.TipoAssociacao, max_length=25)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Evento')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instituicao.Instituicao')),
            ],
        ),
        migrations.AddField(
            model_name='instituicao',
            name='evento',
            field=models.ManyToManyField(through='instituicao.Associacao', to='evento.Evento'),
        ),
    ]