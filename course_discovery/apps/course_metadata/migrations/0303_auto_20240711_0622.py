# Generated by Django 3.2.13 on 2024-07-11 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0302_auto_20240709_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalprogram',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='program',
            name='subject',
        ),
    ]
