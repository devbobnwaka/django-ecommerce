from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from order.models import Order

# Create your views here.

def payment(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        return render(request, 'cart/checkout.html', {})
    else:
        return HttpResponse('Hello')

        