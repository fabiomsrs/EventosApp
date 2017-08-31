# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-31 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comum', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagevento',
            name='evento',
            field=models.ManyToManyField(to='core.Evento'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='evento',
            field=models.ManyToManyField(through='comum.Associacao', to='core.Evento'),
        ),
        migrations.AddField(
            model_name='espacofisico',
            name='espaco_fisico',
            field=models.ManyToManyField(related_name='meus_espacos_fisicos', to='comum.EspacoFisico'),
        ),
        migrations.AddField(
            model_name='associacao',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Evento'),
        ),
        migrations.AddField(
            model_name='associacao',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comum.Instituicao'),
        ),
    ]