# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0010_auto_20171119_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepoimentoParaProjeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome de quem fez o depoimento')),
                ('idade', models.PositiveIntegerField(blank=True, verbose_name='idade de quem fez o depoimento')),
                ('depoimento', models.TextField(verbose_name='depoimento')),
                ('linkVideo', models.URLField(blank=True, verbose_name='link para vídeo do depoimento')),
                ('statement', models.TextField(blank=True, verbose_name='depoimento em inglês')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ong.Projeto', verbose_name='projeto para o qual o depoimento foi feito')),
            ],
            options={
                'verbose_name': 'depoimento para projeto',
                'verbose_name_plural': 'depoimentos para projeto',
                'ordering': ['projeto'],
            },
        ),
    ]