# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0061_migrate_subjects_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserun',
            name='license',
            field=models.CharField(blank=True, db_index=True, max_length=255),
        ),
    ]
