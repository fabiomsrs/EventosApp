# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_atividade', models.CharField(max_length=25)),
                ('descricao', models.CharField(max_length=25)),
                ('valor_atividade', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cupom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desconto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_evento', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='atividade',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Evento'),
        ),
    ]
