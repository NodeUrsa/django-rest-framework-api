# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0003_remove_id_from_field_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='email',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='keyword',
            name='sms',
            field=models.BooleanField(default=False),
        ),
    ]
