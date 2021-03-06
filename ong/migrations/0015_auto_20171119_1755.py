# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0014_auto_20171119_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceitaDeDoacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='data da doação')),
                ('valor', models.FloatField(verbose_name='valor da doação')),
                ('anonimo', models.BooleanField(verbose_name='doação anônima?')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='se não foi anônimo, nome de quem fez a doação')),
                ('utilizacao', models.CharField(choices=[('P1', 'Manutenção administrativa da ONG'), ('P2', 'Aplicação em projetos existentes'), ('P3', 'Criação de novos projetos'), ('P4', 'Aquisição de recursos e materiais'), ('P5', 'Treinamentos para membros da equipe'), ('P6', 'Eventos e comemorações'), ('P7', 'Outras finalidades')], max_length=2, verbose_name='como esse valor foi gasto/utilizado pela ONG')),
                ('meio_pagto', models.CharField(choices=[('M1', 'PayPal'), ('M2', 'Vakinha'), ('M3', 'Boleto'), ('M4', 'Depósito Bancário'), ('M5', 'Transferência Bancária'), ('M5', 'Dinheiro'), ('M7', 'Outro')], max_length=2, verbose_name='meio de pagamento utilizado pelo doador')),
                ('comentarios', models.TextField(blank=True, verbose_name='outras informações (Exemplo: nome do projeto ou evento para o qual o valor foi utilizado)')),
                ('usage', models.CharField(choices=[('E1', 'Administration and maintenance tasks'), ('E2', 'Investments on existing projects'), ('E3', 'Starting of new projects'), ('E4', 'Resources and materials acquisition'), ('E5', 'Training of team members'), ('E6', 'Events and celebrations'), ('E7', 'Other demands')], max_length=2, verbose_name='[INGLÊS] Como esse valor foi gasto/utilizado pela ONG, em ingles')),
                ('pay_method', models.CharField(choices=[('M1', 'PayPal'), ('M2', 'Vakinha'), ('M3', 'Boleto'), ('M4', 'Bank Deposit'), ('M5', 'Bank Transfer'), ('M5', 'Cash'), ('M7', 'Other')], max_length=2, verbose_name='[INGLÊS] Meio de pagamento utilizado pelo doador, em inglês')),
                ('comments', models.TextField(blank=True, verbose_name='[INGLÊS] Outras informações')),
            ],
            options={
                'verbose_name': 'receita de doações',
                'verbose_name_plural': 'receitas de doações',
                'ordering': ['valor'],
            },
        ),
        migrations.AlterField(
            model_name='projeto',
            name='public',
            field=models.CharField(choices=[('E1', 'CHILDREN'), ('E2', 'ADULTS'), ('E3', 'EVERYONE')], max_length=2, verbose_name='[INGLÊS] Público alvo em inglês'),
        ),
    ]
