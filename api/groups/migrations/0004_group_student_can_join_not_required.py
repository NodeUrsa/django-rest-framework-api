# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_set_club_fields_default_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='can_student_join',
            field=models.BooleanField(default=False),
        ),
    ]
