# Generated by Django 2.2.7 on 2019-11-27 14:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental', '0002_auto_20191125_0643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_mark', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('car_issue_year', models.IntegerField()),
                ('car_adding_date', models.DateField(default=datetime.datetime(2019, 11, 27, 14, 39, 10, 712101))),
                ('car_status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Car availability', max_length=1)),
                ('car_renter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['car_mark', 'car_model'],
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date_of_loan', models.DateField(default=datetime.datetime(2019, 11, 27, 14, 39, 10, 713089))),
                ('loan_date_of_return', models.DateField()),
                ('loan_car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rental.Car')),
                ('loan_renter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='loans',
            name='loan_car',
        ),
        migrations.RemoveField(
            model_name='loans',
            name='loan_renter',
        ),
        migrations.DeleteModel(
            name='Cars',
        ),
        migrations.DeleteModel(
            name='Loans',
        ),
    ]