# Generated by Django 3.0.7 on 2021-05-02 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_auto_20210502_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='place_id',
        ),
    ]
