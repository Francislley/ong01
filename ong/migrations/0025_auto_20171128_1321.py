# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0024_auto_20171128_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='email',
            field=models.EmailField(blank=True, max_length=100, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='photo64',
            field=models.TextField(null=True, verbose_name='foto (se preenchido, foto já existe no sistema)'),
        ),
    ]
