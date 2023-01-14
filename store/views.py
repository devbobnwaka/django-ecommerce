from django.shortcuts import render
from store.models import Product

# Create your views here.

def single_product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product':product
    }
    return render(request, 'product/product.html', context)
