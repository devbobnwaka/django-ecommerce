from django.shortcuts import render, redirect

# Create your views here.

def add_cart(request, slug):
    
    if 'slug' in request.session:
        if slug not in request.session['slug']:
            request.session['slug'].append(slug)
    else:
        request.session['slug'] = [slug]
    # del request.session['slug']
    request.session.modified = True

    return redirect(request.META.get('HTTP_REFERER'))


def cart(request):
    return render(request, 'cart/cart.html', {})
