# Generated by Django 3.2.8 on 2022-10-11 01:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manufacturer', '0012_auto_20221008_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybydayproducts',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 10, 11)),
        ),
        migrations.AlterField(
            model_name='daybydayproductsdistribute',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 10, 11)),
        ),
        migrations.AlterField(
            model_name='distribute',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2022, 10, 11)),
        ),
        migrations.AlterField(
            model_name='manufacturerstock',
            name='production_date',
            field=models.DateField(verbose_name=datetime.date(2022, 10, 11)),
        ),
    ]
