# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 09:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20170122_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='comment',
            new_name='text',
        ),
    ]
