# Generated by Django 3.2.8 on 2022-09-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manufacturer', '0002_auto_20220925_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribute',
            name='user',
        ),
        migrations.RemoveField(
            model_name='distribute',
            name='username',
        ),
        migrations.AddField(
            model_name='distribute',
            name='distributor_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='createdproducts',
            name='Product_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='createdproducts',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='createdproducts',
            name='manufacturer_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='createdproducts',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='createdproducts',
            name='production_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='distribute',
            name='manufacturer_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='distribute',
            name='product_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='distribute',
            name='product_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='distribute',
            name='product_quantity',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='distribute',
            name='total_price',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='setproduct',
            name='Product_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='setproduct',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='setproduct',
            name='manufacturer_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='setproduct',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='totalproducts',
            name='manufacturer_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='totalproducts',
            name='product_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='totalproducts',
            name='product_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='totalproducts',
            name='product_quantity',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]