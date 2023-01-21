from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from order.models import Order

# Create your views here.

# def payment(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':

#         context = {
#             'paystack_public_key': settings.PAYSTACK_SECRET_KEY
#         }
#         return render(request, 'cart/make_payment.html', context)
#     else:
#         return render(request, 'cart/checkout.html', {})

        