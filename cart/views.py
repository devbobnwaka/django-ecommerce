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
    product = Product.objects.get(slug=slug)
    if 'slug' in request.session:
        if slug not in request.session['slug']:
            request.session['slug'].append(slug)
            request.session['quantity'].update({slug:1})
            request.session['discount_price_total'].update({slug: product.discount_price()})
            print(request.session['slug'])
            print(request.session['quantity'])
            print(request.session['discount_price_total'])
    else:
        request.session['slug'] = [slug]
        request.session['quantity'] =  {slug: 1}
        request.session['discount_price_total'] = {slug: product.discount_price()}
        print(request.session['slug'])
        print(request.session['quantity'])
        print(request.session['discount_price_total'])

    # del request.session['slug']
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER'))


def remove_cart(request, slug):
    request.session['slug'].remove(slug)
    request.session['quantity'].pop(slug)
    request.session['discount_price_total'].pop(slug)
    print(request.session['slug'])
    print(request.session['quantity'])
    print(request.session['discount_price_total'])

    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER'))


def increase_cart_quantity(request, slug):
    product = Product.objects.get(slug=slug)
    request.session['quantity'][slug] += 1
    request.session['discount_price_total'][slug] = product.discount_price() * request.session['quantity'][slug]
    
    print(request.session['slug'])
    print(request.session['quantity'])
    print(request.session['discount_price_total'])
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER'))


def decrease_cart_quantity(request, slug):
    product = Product.objects.get(slug=slug)
    if request.session['quantity'][slug] > 1:
        request.session['quantity'][slug] -= 1
        request.session['discount_price_total'][slug] = product.discount_price() * request.session['quantity'][slug]
    else:
        request.session['slug'].remove(slug)
        request.session['quantity'].pop(slug, 'quantity not found')
        request.session['discount_price_total'].pop(slug, 'discount_price_total not found')

    print(request.session['slug'])
    print(request.session['quantity'])
    print(request.session['discount_price_total'])

    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER'))


