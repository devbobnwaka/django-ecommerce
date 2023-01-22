from django.db import models
# from store.models import Product
# from django.db.models.signals import pre_save, post_save
# from utils.utils import slugify_instance_title

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


# def category_post_pre_save(sender, instance, *args, **kwargs):
#     if instance.slug is None:
#         slugify_instance_title(instance)

# pre_save.connect(category_post_pre_save, sender=Category) 

# def category_post_post_save(sender, instance, created, *args, **kwargs):
#     if created:
#         slugify_instance_title(instance, save=True)

# post_save.connect(category_post_post_save, sender=Category) 