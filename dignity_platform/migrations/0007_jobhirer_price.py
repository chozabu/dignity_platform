# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dignity_platform', '0006_person_self_support'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobhirer',
            name='price',
            field=models.FloatField(default=15.0),
        ),
    ]
