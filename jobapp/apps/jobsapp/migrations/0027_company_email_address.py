# Generated by Django 4.2.7 on 2023-12-11 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0026_merge_20231211_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email_address',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
