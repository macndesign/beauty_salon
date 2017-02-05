# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('description', models.TextField(verbose_name='descrição')),
                ('value', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='valor')),
            ],
            options={
                'verbose_name': 'Despesa',
            },
        ),
    ]