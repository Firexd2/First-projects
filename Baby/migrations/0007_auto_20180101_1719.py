# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-01 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Baby', '0006_auto_20180101_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='babyeat',
            name='volume',
        ),
        migrations.AddField(
            model_name='babyeat',
            name='volume_mixture',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='babyeat',
            name='volume_porridge',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='babyeat',
            name='volume_puree',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]