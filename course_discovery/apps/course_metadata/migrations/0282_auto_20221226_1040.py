# Generated by Django 3.2.13 on 2022-12-26 10:40

import course_discovery.apps.course_metadata.fields
import course_discovery.apps.course_metadata.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0281_auto_20221226_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprogram',
            name='certificte_overview',
            field=course_discovery.apps.course_metadata.fields.NullHtmlField(blank=True, default=None, null=True, validators=[course_discovery.apps.course_metadata.validators.validate_html], verbose_name='Program Certificate Overview'),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='ebooks_overview',
            field=course_discovery.apps.course_metadata.fields.NullHtmlField(blank=True, default=None, null=True, validators=[course_discovery.apps.course_metadata.validators.validate_html], verbose_name='E-Books from EBC Reader Overview'),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='live_class_overview',
            field=course_discovery.apps.course_metadata.fields.NullHtmlField(blank=True, default=None, null=True, validators=[course_discovery.apps.course_metadata.validators.validate_html], verbose_name='Demo Live Classes Overview'),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='placement_overview',
            field=course_discovery.apps.course_metadata.fields.NullHtmlField(blank=True, default=None, null=True, validators=[course_discovery.apps.course_metadata.validators.validate_html], verbose_name='INTERNSHIP & PLACEMENT PARTNERS Overview'),
        ),
        migrations.AlterField(
            model_name='program',
            name='certificte_overview',
            field=course_discovery.apps.course_metadata.fields.NullHtmlField(blank=True, default=None, null=True, validators=[course_discovery.apps.course_metadata.validators.validate_html], verbose_name='Program Certificate Overview'),
        ),
        migrations.AlterField(
            model_name='program',
            name='ebooks_overview',
            field=course_discovery.apps.course_metadata.fields.NullHtmlField(blank=True, default=None, null=True, validators=[course_discovery.apps.course_metadata.validators.validate_html], verbose_name='E-Books from EBC Reader Overview'),
        ),
        migrations.AlterField(
            model_name='program',
            name='live_class_overview',
            field=course_discovery.apps.course_metadata.fields.NullHtmlField(blank=True, default=None, null=True, validators=[course_discovery.apps.course_metadata.validators.validate_html], verbose_name='Demo Live Classes Overview'),
        ),
        migrations.AlterField(
            model_name='program',
            name='placement_overview',
            field=course_discovery.apps.course_metadata.fields.NullHtmlField(blank=True, default=None, null=True, validators=[course_discovery.apps.course_metadata.validators.validate_html], verbose_name='INTERNSHIP & PLACEMENT PARTNERS Overview'),
        ),
    ]