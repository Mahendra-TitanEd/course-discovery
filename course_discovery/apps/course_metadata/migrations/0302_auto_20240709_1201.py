# Generated by Django 3.2.13 on 2024-07-09 12:01

from django.db import migrations, models
import django.db.models.deletion
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0301_auto_20240529_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='categories',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, related_name='categories', to='course_metadata.Subject'),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='subject',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course_metadata.subject', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='program',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course_metadata.subject', verbose_name='Category'),
        ),
    ]