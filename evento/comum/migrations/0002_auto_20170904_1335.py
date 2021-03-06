# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 16:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170904_1335'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='associacao',
            name='evento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Evento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='associacao',
            name='instituicao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='comum.Instituicao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='espacofisico',
            name='espaco_fisico',
            field=models.ManyToManyField(related_name='meus_espacos_fisicos', to='comum.EspacoFisico'),
        ),
        migrations.AddField(
            model_name='instituicao',
            name='evento',
            field=models.ManyToManyField(through='comum.Associacao', to='core.Evento'),
        ),
        migrations.AddField(
            model_name='tagevento',
            name='evento',
            field=models.ManyToManyField(to='core.Evento'),
        ),
        migrations.AddField(
            model_name='tagusuario',
            name='usuario',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
