# Generated by Django 3.2.13 on 2024-10-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0307_auto_20241008_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprogram',
            name='enrollment_btn_title',
            field=models.CharField(default='Enrollment Starts Soon', help_text="This field allows admins to set a custom title for the enrollment button on the program about page. If the program's enrollment start date is in the future, this message will replace 'Enroll Now'.", max_length=255, verbose_name='Enrollment Button Title'),
        ),
        migrations.AddField(
            model_name='program',
            name='enrollment_btn_title',
            field=models.CharField(default='Enrollment Starts Soon', help_text="This field allows admins to set a custom title for the enrollment button on the program about page. If the program's enrollment start date is in the future, this message will replace 'Enroll Now'.", max_length=255, verbose_name='Enrollment Button Title'),
        ),
    ]
