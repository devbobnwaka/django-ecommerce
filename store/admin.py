from django.contrib import admin
from .models import Product, ProductImage

# Register your models here.
class ProductImageInline(admin.StackedInline):
    extra = 1
    model = ProductImage
    list_display = ('product_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('product_name', 'stock', 'price', 'discount_type')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ['product_name']
    # raw_id_fields = ('category_id',)

# admin.site.register(Product)

# admin.site.register(ProductImage)

