from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Product(models.Model):
    '''
    product name
    product description
    product price
    product main photo
    product extra photoes
    product category
    
    optional features
    discount
    '''
    product_id = models.AutoField(primary_key=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=1000, null=False)
    product_description = models.CharField(max_length=10000, null=False)
    product_price = models.IntegerField(null=False)
    product_discount = models.IntegerField(null=True, default=0)
    product_manufacturing_date = models.DateTimeField()
    product_upload_time = models.DateTimeField(default=None)
    product_cover_photo = models.ImageField()
    product_extra_photos = models.ImageField(null=True)
    product_category = models.CharField(default=None, null=True, max_length=1000)

    def __str__(self) -> str:
        return self.product_id


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = Product().product_name
    product_price = Product().product_price
    product_discount = Product().product_discount

    def __str__(self) -> str:
        return self.user