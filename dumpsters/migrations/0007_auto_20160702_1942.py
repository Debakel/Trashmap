# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dumpsters', '0006_auto_20160510_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='value',
            field=models.CharField(choices=[('good', 'Good'), ('senseless', 'Not good'), ('average', 'Neutral')],
                                   max_length=255),
        ),
    ]
