import datetime

from django.db import models
from django.contrib.auth.models import User

from products.models import Products
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return str(self.id)
        
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)
    timestamp = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    
    def __unicode__(self):
        return str(self.product.name)
    
