from django.db import models
from django.contrib.auth.models import User


class Sklad(models.Model):
    type_product = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.type_product
    class Meta:
        verbose_name = "Склади"

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    count = models.PositiveIntegerField(default=0)
    sklad = models.ForeignKey(Sklad,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name    
    class Meta:
        verbose_name = "Продукти"

class Orders(models.Model):
    name = models.CharField(max_length=200)
    adress_order = models.CharField(max_length=200)
    priority = models.PositiveIntegerField(default=0)
    proudct = models.ForeignKey(Product,on_delete=models.CASCADE)  
    user =  models.ForeignKey(User,on_delete=models.CASCADE)      

