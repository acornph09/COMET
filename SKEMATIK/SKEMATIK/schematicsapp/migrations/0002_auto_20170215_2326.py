# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schematicsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schematicmodel',
            name='schematic_description',
            field=models.CharField(default='no description', max_length=250),
        ),
        migrations.AddField(
            model_name='schematicmodel',
            name='schematic_name',
            field=models.CharField(default='no name', max_length=30),
        ),
    ]
