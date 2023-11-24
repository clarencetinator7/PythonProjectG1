# Generated by Django 4.2.7 on 2023-11-24 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0011_alter_education_education_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='education_level',
            field=models.CharField(choices=[('HS', 'High School'), ('UG', 'Bachelors'), ('PG', 'Master'), ('CF', 'Certificate'), ('AS', 'Associates')], max_length=4),
        ),
    ]
