# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2024-02-09 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0012_auto_20230710_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('f_id', models.IntegerField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
        ),
    ]
