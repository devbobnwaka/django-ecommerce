from django.shortcuts import render, redirect

# Create your views here.

def add_cart(request, slug):
    print('Here')
    print(request.session)
    return redirect('home')
