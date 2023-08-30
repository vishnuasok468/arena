from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_details(models.Model):
    d_address=models.CharField(max_length=300)
    d_number=models.CharField(max_length=20)
    d_user=models.ForeignKey(User,on_delete=models.CASCADE)

class category(models.Model):
    d_category=models.CharField(max_length=200)

class products(models.Model):
    d_product=models.CharField(max_length=200)
    d_description=models.CharField(max_length=300)
    d_price=models.IntegerField()
    d_img=models.ImageField(upload_to='images/')
    d_category=models.ForeignKey(category,on_delete=models.CASCADE)

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE)