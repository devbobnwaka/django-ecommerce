from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from .models import Account

# Create your views here.
def register(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        data = request.POST.dict()
        email = data.get('register-email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get('phone_number')
        password1 = data.get('register-password1')
        password2 = data.get('register-password2')
        if password1 and password2 and password1 != password2:
            messages.error(request, "Passwords don't match")
            return redirect('login')
        try:
            Account.objects.create_user(email=email, first_name=first_name, last_name=last_name, phone_number=phone_number, password=password1)
            messages.success(request, 'User account created successfully, you can now login!!! ')
        except Exception as e:
            messages.error(request, f'{e} Account creation failed!!! ')
        return redirect('login')
    context = {}
    return render(request, "accounts/login.html", context)


def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        login_data = request.POST.dict()
        email = login_data.get('singin-email')
        # print(email)
        password = login_data.get('singin-password')
        # print(password)
        user = authenticate(request, email=email, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'accounts/login.html', {})


@login_required
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        logout(request)
        return redirect('home')
    return render(request, "accounts/logout.html", {})