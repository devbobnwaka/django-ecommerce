from django.shortcuts import render, redirect
from store.models import Product, ProductImage

# Create your views here.
def cart(request):
    quantity_dict = request.session.get('quantity')
    products = Product.objects.filter(slug__in=request.session['slug'])
    pro = {'products':products}
    context = quantity_dict | pro
    return render(request, 'cart/cart.html', context)


def add_cart(request, slug):
    
    if 'slug' in request.session:
        if slug not in request.session['slug']:
            request.session['slug'].append(slug)
            request.session['quantity'][slug] = 1
    else:
        request.session['slug'] = [slug]
        request.session['quantity'][slug] = 1
        
    # del request.session['slug']
    request.session.modified = True

    return redirect(request.META.get('HTTP_REFERER'))


def remove_cart(request, slug):
    request.session['slug'].remove(slug)
    del request.session['quantity'][slug]
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER'))


def increase_cart_quantity(request, slug):
    request.session['quantity'][slug] += 1
    print(request.session['quantity'][slug])
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER'))


def decrease_cart_quantity(request, slug):
    if request.session['quantity'][slug] > 1:
        request.session['quantity'][slug] -= 1
        print(request.session['slug'])
    else:
        request.session['slug'].remove(slug)
        del request.session['quantity'][slug]
        print(request.session['slug'])
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER'))


