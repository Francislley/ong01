# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0023_auto_20171127_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='email',
            field=models.EmailField(blank=True, max_length=100, verbose_name='email'),
        ),
    ]
