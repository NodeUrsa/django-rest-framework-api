# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20170207_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='show_student_association',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='club',
            name='show_student_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='club',
            name='show_student_id',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='club',
            name='show_student_mobile',
            field=models.BooleanField(default=False),
        ),
    ]
