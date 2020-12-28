from django.db import models

# Create your models here.
#let us create a model i.e class otherwise for dynamic data this is enough
class market:
    img : str
    name : str
# create a model for sign up to link db only
class Customer(models.Model):
    user=models.CharField('Username',max_length=120)
    mobileno=models.CharField('Mobile no',max_length=120)
    address=models.CharField('Address',max_length=250)
class Items(models.Model):
    item_name=models.CharField('Item_name',max_length=120)
    item_id=models.IntegerField(default=1,null=True,blank=True)
    img_name=models.CharField('Image_name',max_length=120)
    price=models.IntegerField(default=1,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    brand_name=models.CharField('brand_name',max_length=120)
    class_name=models.CharField('class_name',max_length=120)
class Cart(models.Model):
    user=models.CharField('Username',max_length=120)
    item_id=models.IntegerField(default=1,null=True,blank=True)
class Buy(models.Model):
    user=models.CharField('Username',max_length=120)
    item_id=models.IntegerField(default=1,null=True,blank=True)
    # userquantity and price and address and phoneno and email and transaction id attributes 
    user_quantity =models.IntegerField(default=1,null=True,blank=True)
    price=models.IntegerField(default=1,null=True,blank=True)
    address=models.CharField('Address',max_length=120)
    mobileno=models.CharField('Mobile no',max_length=120)
    email=models.CharField('Email',max_length=120)
    transaction_id=models.CharField('Transacton_id',max_length=120)
class Stock(models.Model):
    item_id=models.IntegerField(default=1,null=True,blank=True)
    stock_quantity=models.IntegerField(default=1,null=True,blank=True)