# Generated by Django 3.0.7 on 2021-04-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0018_auto_20210416_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='one_strong_point_for_recommendations',
            field=models.CharField(blank='True', default='In 2-3 words', max_length=100),
        ),
    ]
