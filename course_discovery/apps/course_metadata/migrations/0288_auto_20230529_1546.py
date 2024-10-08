# Generated by Django 3.2.13 on 2023-05-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0287_auto_20230423_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='designation',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='salutation',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Title'),
        ),
    ]