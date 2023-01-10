from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
    PERCENTAGE = 'PER'
    FIXED = 'FIX'
    NONE = 'NIL'
    DISCOUNT_TYPE_CHOICE = [
        (NONE,"NONE"),
        (PERCENTAGE,"PERCENTAGE"),
        (FIXED,"FIXED"),
    ]
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    discount_type = models.CharField(max_length=3, choices=DISCOUNT_TYPE_CHOICE, default=None)
    discount_value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
