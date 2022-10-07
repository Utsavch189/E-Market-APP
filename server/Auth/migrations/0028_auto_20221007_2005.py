# Generated by Django 3.2.8 on 2022-10-07 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0027_auto_20221007_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='email',
            new_name='target',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='phone',
        ),
        migrations.AlterField(
            model_name='otp',
            name='created_at',
            field=models.TimeField(verbose_name=datetime.datetime(2022, 10, 7, 20, 5, 50, 494498)),
        ),
    ]