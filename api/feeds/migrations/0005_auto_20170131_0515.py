# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 05:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_rename post comment to text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_campus',
            new_name='campus',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_faculty',
            new_name='faculty',
        ),
    ]