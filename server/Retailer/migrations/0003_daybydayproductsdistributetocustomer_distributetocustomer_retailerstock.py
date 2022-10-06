# Generated by Django 3.2.8 on 2022-10-06 02:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Retailer', '0002_delete_distributetoretailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayByDayProductsDistributeToCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, max_length=30, null=True)),
                ('retailer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('product_quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateField(verbose_name=datetime.date(2022, 10, 6))),
            ],
        ),
        migrations.CreateModel(
            name='DistributeToCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('product_id', models.CharField(blank=True, max_length=30, null=True)),
                ('product_quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('total_price', models.CharField(blank=True, max_length=10, null=True)),
                ('calculation_status', models.BooleanField(default=False)),
                ('date', models.DateField(verbose_name=datetime.date(2022, 10, 6))),
            ],
        ),
        migrations.CreateModel(
            name='RetailerStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, max_length=30, null=True)),
                ('product_name', models.CharField(blank=True, max_length=25, null=True)),
                ('retailer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('distributor_id', models.CharField(blank=True, max_length=50, null=True)),
                ('product_quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('total_price', models.CharField(blank=True, max_length=10, null=True)),
                ('price_per_product', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateField(verbose_name=datetime.date(2022, 10, 6))),
            ],
        ),
    ]
