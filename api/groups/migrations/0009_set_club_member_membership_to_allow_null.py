# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_set_club_member_paid_default_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubmember',
            name='membership_to',
            field=models.IntegerField(null=True),
        ),
    ]
