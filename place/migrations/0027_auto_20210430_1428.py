# Generated by Django 3.0.7 on 2021-04-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0026_auto_20210417_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='feature4',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='feature5',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
