# Generated by Django 4.2.7 on 2023-12-11 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0022_alerts_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
