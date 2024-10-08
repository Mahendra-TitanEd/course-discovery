# Generated by Django 3.2.13 on 2023-07-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0289_auto_20230705_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprogram',
            name='partner_display',
            field=models.CharField(blank=True, help_text='Enter the programme partner you want to have on the show." The partner you chose in previous partner is overridden by this setting. To use the chosen partner, leave it empty.', max_length=512, null=True, verbose_name='Partner Display String'),
        ),
        migrations.AddField(
            model_name='historicalprogram',
            name='tax_info',
            field=models.CharField(blank=True, default='Price not inclusive of GST', max_length=512, null=True, verbose_name='Tax Information'),
        ),
        migrations.AddField(
            model_name='program',
            name='partner_display',
            field=models.CharField(blank=True, help_text='Enter the programme partner you want to have on the show." The partner you chose in previous partner is overridden by this setting. To use the chosen partner, leave it empty.', max_length=512, null=True, verbose_name='Partner Display String'),
        ),
        migrations.AddField(
            model_name='program',
            name='tax_info',
            field=models.CharField(blank=True, default='Price not inclusive of GST', max_length=512, null=True, verbose_name='Tax Information'),
        ),
    ]