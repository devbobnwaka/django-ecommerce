from django.shortcuts import render, redirect
from store.models import Product, ProductImage

# Create your views here.
def cart(request):
    print(request.session.get('slug'))
    products = Product.objects.filter(slug__in=request.session['slug'])
    context = {
        'products':products,
    }
    return render(request, 'cart/cart.html', context)


def add_cart(request, slug):
    
    if 'slug' in request.session:
        if slug not in request.session['slug']:
            request.session['slug'].append(slug)
    else:
        request.session['slug'] = [slug]
    # del request.session['slug']
    request.session.modified = True

    return redirect(request.META.get('HTTP_REFERER'))


def remove_cart(request, slug):
    request.session['slug'].remove(slug)
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER'))
