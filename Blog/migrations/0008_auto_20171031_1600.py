# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20171031_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'date'},
        ),
        migrations.AddField(
            model_name='post',
            name='image_resize',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
