# Generated by Django 3.2.8 on 2022-10-11 01:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Retailer', '0005_auto_20221008_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybydayproductsdistributetocustomer',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 10, 11)),
        ),
        migrations.AlterField(
            model_name='distributetocustomer',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 10, 11)),
        ),
        migrations.AlterField(
            model_name='retailerstock',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 10, 11)),
        ),
    ]