# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='food_id',
            field=models.CharField(auto_created=True, max_length=10, primary_key=True, serialize=False),
        ),
    ]
