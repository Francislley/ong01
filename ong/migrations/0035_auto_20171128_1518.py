# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0034_membro_possuiphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='activity',
            field=models.CharField(blank=True, max_length=100, verbose_name='atividade ou função que exerce na ONG, em inglês'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='country',
            field=models.CharField(blank=True, max_length=100, verbose_name='país, em inglês'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='statement',
            field=models.TextField(blank=True, verbose_name='depoimento sobre a ONG, em inglês'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='description',
            field=models.TextField(blank=True, verbose_name='descrição, em inglês'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='nome do projeto, em inglês'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='nome do projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='public',
            field=models.CharField(choices=[('E1', 'CHILDREN'), ('E2', 'ADULTS'), ('E3', 'EVERYONE')], max_length=2, verbose_name='público alvo, em inglês'),
        ),
    ]
