from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

# Create your views here.
def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        login_data = request.POST.dict()
        email = login_data.get('singin-email')
        password = login_data.get('singin-password')
        user = authenticate(request, email=email, password=password)
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