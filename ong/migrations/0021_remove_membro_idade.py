# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0020_membro_idade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membro',
            name='idade',
        ),
    ]