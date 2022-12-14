from django.db import models
from datetime import date


class SetProduct(models.Model):
    manufacturer_id=models.CharField(null=True,blank=True,max_length=25)
    name=models.CharField(null=True,blank=True,max_length=25)
    price=models.CharField(null=True,blank=True,max_length=10)
    description=models.CharField(null=True,blank=True,max_length=50)
    Product_id=models.CharField(null=True,blank=True,max_length=30)
    
    def __str__(self):
        return self.name+' '+'(BY:'+self.manufacturer_id+')'



class ManufacturerStock(models.Model):
    manufacturer_id=models.CharField(null=True,blank=True,max_length=25)
    Product_id=models.CharField(null=True,blank=True,max_length=30)
    name=models.CharField(null=True,blank=True,max_length=25)
    price=models.CharField(null=True,blank=True,max_length=10)
    description=models.CharField(null=True,blank=True,max_length=50)
    production_no=models.CharField(null=True,blank=True,max_length=20)
    production_date=models.DateField(date.today())

    def __str__(self):
        return self.name+' '+'(BY:'+self.manufacturer_id+')'


class Distribute(models.Model):
    distributor_id=models.CharField(null=True,blank=True,max_length=25)
    product_id=models.CharField(null=True,blank=True,max_length=30)
    manufacturer_id=models.CharField(null=True,blank=True,max_length=25)
    product_quantity=models.CharField(null=True,blank=True,max_length=20)
    total_price=models.CharField(null=True,blank=True,max_length=20)
    calculation_status=models.BooleanField(default=False)
    date=models.DateField(date.today())

    def __str__(self):
        return '('+self.product_id+')'+' '+'( from:'+self.manufacturer_id+')'


class DayByDayProducts(models.Model):
    product_id=models.CharField(null=True,blank=True,max_length=30)
    manufacturer_id=models.CharField(null=True,blank=True,max_length=25)
    product_name=models.CharField(null=True,blank=True,max_length=25)
    product_quantity=models.CharField(null=True,blank=True,max_length=20)
    date=models.DateField(date.today())
    
    def __str__(self) -> str:
        return self.product_name


class DayByDayProductsDistribute(models.Model):
    product_id=models.CharField(null=True,blank=True,max_length=30)
    manufacturer_id=models.CharField(null=True,blank=True,max_length=25)
    product_quantity=models.CharField(null=True,blank=True,max_length=20)
    distributor_id=models.CharField(null=True,blank=True,max_length=25)
    date=models.DateField(date.today())
    
    def __str__(self):
        return '('+self.product_id+')'+' '+'( from:'+self.manufacturer_id+')'
