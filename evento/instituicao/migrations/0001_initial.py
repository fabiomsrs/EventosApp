# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import instituicao.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Associacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_associacao', enumfields.fields.EnumField(default='default', enum=instituicao.models.TipoAssociacao, max_length=25)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_instituicao', models.CharField(max_length=25)),
                ('uf', models.CharField(max_length=2)),
                ('evento', models.ManyToManyField(through='instituicao.Associacao', to='evento.Evento')),
            ],
        ),
        migrations.AddField(
            model_name='associacao',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instituicao.Instituicao'),
        ),
    ]
