

def counter(request):
    cart_count = 0
    for val in request.session['quantity'].values():
        cart_count += val
    return dict(cart_count=cart_count) 