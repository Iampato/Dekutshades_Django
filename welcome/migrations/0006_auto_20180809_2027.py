# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-09 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0005_auto_20180809_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(default='slider', max_length=250),
        ),
    ]