# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160524_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gcdseries',
            name='cover_url',
        ),
        migrations.AddField(
            model_name='gcdseries',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover/series'),
        ),
    ]
