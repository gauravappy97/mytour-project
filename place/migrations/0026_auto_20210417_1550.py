# Generated by Django 3.0.7 on 2021-04-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0025_auto_20210417_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='feature4',
            field=models.CharField(blank='True', default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='feature5',
            field=models.CharField(blank='True', default=' ', max_length=100),
        ),
    ]
