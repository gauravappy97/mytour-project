# Generated by Django 3.0.7 on 2021-04-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0017_auto_20210416_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='Reason2',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='Reason3',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='Reason4',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='Reason5',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='Reason_to_visit',
            field=models.CharField(default='like sake brewing', max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='feature2',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='feature3',
            field=models.CharField(default=' ', max_length=100),
        ),
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
        migrations.AlterField(
            model_name='place',
            name='place_photo_1',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_photo_2',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_photo_3',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_photo_4',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
