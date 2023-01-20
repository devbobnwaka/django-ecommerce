from django.db import models
from accounts.models import Account
from store.models import Product

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    ref = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class OrderProduct(models.Model):
    oder = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
