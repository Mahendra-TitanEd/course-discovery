# Generated by Django 3.2.13 on 2024-02-08 08:44

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0297_auto_20240108_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprogram',
            name='program_about',
            field=models.TextField(blank=True, null=True, verbose_name='Overview'),
        ),
        migrations.AddField(
            model_name='program',
            name='program_about',
            field=models.TextField(blank=True, null=True, verbose_name='Overview'),
        ),
        migrations.AlterField(
            model_name='historicalprogram',
            name='overview',
            field=models.TextField(blank=True, null=True, verbose_name='Program About'),
        ),
        migrations.AlterField(
            model_name='program',
            name='overview',
            field=models.TextField(blank=True, null=True, verbose_name='Program About'),
        ),
        migrations.CreateModel(
            name='VideosBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=1024)),
                ('iframe_url', models.TextField(verbose_name='Iframe url')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_metadata.program')),
            ],
            options={
                'verbose_name': 'VideoBlock',
                'verbose_name_plural': 'Videos Block',
            },
        ),
    ]