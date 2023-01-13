from django.urls import path
from . import views

urlpatterns = [
    path('add_cart/<slug:slug>', views.add_cart, name="add_cart"),
    path('', views.cart, name="cart"),
]
