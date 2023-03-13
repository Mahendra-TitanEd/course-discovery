# Generated by Django 3.2.13 on 2022-12-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0282_auto_20221226_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalprogram',
            name='live_class_overview',
        ),
        migrations.RemoveField(
            model_name='program',
            name='live_class_overview',
        ),
        migrations.AddField(
            model_name='historicalprogram',
            name='overview_2',
            field=models.TextField(blank=True, null=True, verbose_name='Program Overview 2'),
        ),
        migrations.AddField(
            model_name='program',
            name='overview_2',
            field=models.TextField(blank=True, null=True, verbose_name='Program Overview 2'),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='assignment_due',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='certificte_overview',
            field=models.TextField(blank=True, null=True, verbose_name='Program Certificate Overview'),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='ebooks_overview',
            field=models.TextField(blank=True, null=True, verbose_name='E-Books from EBC Reader Overview'),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='placement_overview',
            field=models.TextField(blank=True, null=True, verbose_name='INTERNSHIP & PLACEMENT PARTNERS Overview'),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='assignment_due',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='certificte_overview',
            field=models.TextField(blank=True, null=True, verbose_name='Program Certificate Overview'),
        ),
        migrations.AlterField(
            model_name='program',
            name='ebooks_overview',
            field=models.TextField(blank=True, null=True, verbose_name='E-Books from EBC Reader Overview'),
        ),
        migrations.AlterField(
            model_name='program',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='placement_overview',
            field=models.TextField(blank=True, null=True, verbose_name='INTERNSHIP & PLACEMENT PARTNERS Overview'),
        ),
        migrations.AlterField(
            model_name='program',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]