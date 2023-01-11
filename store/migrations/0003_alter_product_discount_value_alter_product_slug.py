# Generated by Django 4.1.5 on 2023-01-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_discount_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
