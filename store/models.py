from django.db import models
from django.db.models.signals import pre_save, post_save
from utils.utils import slugify_instance_product_name
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
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    discount_type = models.CharField(max_length=3, choices=DISCOUNT_TYPE_CHOICE, default=None)
    discount_value = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def discount_price(self):
        if self.discount_type == 'FIX':
            return self.discount_value
        elif self.discount_type == 'PER':
            return self.price - round((self.discount_value/100) * self.price)

    def discount_per(self):
        if self.discount_type == 'PER':
            return self.discount_value
        elif self.discount_type == 'FIX':
            return 100 - round((self.discount_value/self.price) * 100)





class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.product

def product_pre_save(sender, instance, *args, **kwargs):
    print(sender)
    if instance.slug is None:
        print()
        slugify_instance_product_name(instance)

pre_save.connect(product_pre_save, sender=Product) 

def product_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_product_name(instance, save=True)

post_save.connect(product_post_save, sender=Product) 
