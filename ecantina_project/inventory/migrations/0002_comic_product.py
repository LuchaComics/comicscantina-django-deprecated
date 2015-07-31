# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='product',
            field=models.ForeignKey(default=1, to='inventory.Product'),
            preserve_default=False,
        ),
    ]
