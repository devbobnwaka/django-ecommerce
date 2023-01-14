from django.shortcuts import render
from store.models import Product, ProductImage

# Create your views here.
def category(request):
    products = Product.objects.all()

    context = {
        'products':products
    }
    return render(request, 'category/category.html', context)