# Generated by Django 4.1.5 on 2023-01-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_type',
            field=models.CharField(choices=[('NIL', 'NONE'), ('PER', 'PERCENTAGE'), ('FIX', 'FIXED')], default=None, max_length=3),
        ),
    ]
