from django.shortcuts import render
from django.db.models import Q
from .models import Category
from store.models import Product, ProductImage

# Create your views here.
def category(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories': categories,
    }
    return render(request, 'category/category.html', context)

def single_cat(request, slug):
    products = Product.objects.filter(category_id=slug)
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories': categories,
    }
    return render(request, 'category/category.html', context)
