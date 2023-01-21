

def custom_context_processor(request):
    sub_total = 0
    cart_count = 0
    if 'quantity' in request.session:
        for val in request.session['quantity'].values():
            cart_count += val
    
    if 'discount_price_total' in request.session:
        for price in request.session['discount_price_total'].values():
            sub_total += price
    return dict(cart_count=cart_count, sub_total="{:,}".format(sub_total), sub_total_int=int(sub_total)) 


# def sub_total(request):
#     sub_total = 0
#     for price in request.session['discount_price_total'].values():
#         sub_total += price
#         print(price)
#     return dict(sub_total=sub_total)