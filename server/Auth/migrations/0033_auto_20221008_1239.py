# Generated by Django 3.2.8 on 2022-10-08 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0032_auto_20221008_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='tried',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='otp',
            name='created_at_date',
            field=models.TimeField(default=datetime.time(12, 39, 36, 600784)),
        ),
    ]