# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_kotelnikov', '0006_auto_20170309_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]