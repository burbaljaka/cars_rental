# Generated by Django 2.2.7 on 2019-11-28 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0010_auto_20191128_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_adding_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 28, 12, 3, 30, 969024)),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_rent_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
