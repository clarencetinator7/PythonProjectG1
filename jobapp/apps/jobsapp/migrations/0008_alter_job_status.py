# Generated by Django 4.2.7 on 2023-12-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0007_alter_job_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=8),
        ),
    ]
