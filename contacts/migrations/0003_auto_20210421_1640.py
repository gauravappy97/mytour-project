# Generated by Django 3.0.7 on 2021-04-21 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20210421_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='costumer_nedd',
            new_name='costumer_need',
        ),
    ]
