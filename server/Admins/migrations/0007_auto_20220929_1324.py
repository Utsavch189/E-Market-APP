# Generated by Django 3.2.8 on 2022-09-29 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0006_auto_20220928_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedusers',
            name='approved_at',
            field=models.DateField(verbose_name=datetime.date(2022, 9, 29)),
        ),
        migrations.AlterField(
            model_name='deletedusers',
            name='deleted_at',
            field=models.DateField(verbose_name=datetime.date(2022, 9, 29)),
        ),
    ]