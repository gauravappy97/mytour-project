# Generated by Django 3.0.7 on 2021-04-17 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0019_auto_20210417_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='weather_APR_JUL',
        ),
        migrations.RemoveField(
            model_name='place',
            name='weather_AUG_NOV',
        ),
        migrations.RemoveField(
            model_name='place',
            name='weather_DEC_MAR',
        ),
    ]
