# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 13:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0002_make_keyword_subject_nullable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='subject',
            field=models.ForeignKey(null=True,
                on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='subjects.Subject'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='uni',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='universities.University'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to=settings.AUTH_USER_MODEL),
        ),
    ]
