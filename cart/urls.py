from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('add_cart/<slug:slug>/', views.add_cart, name="add_cart"),
    path('checkout/', views.checkout, name='checkout'),
    path('remove_cart/<slug:slug>/', views.remove_cart, name="remove_cart"),
    path('increase_cart_quantity/<slug:slug>', views.increase_cart_quantity, name="increase_cart"),
    path('decrease_cart_quantity/<slug:slug>', views.decrease_cart_quantity, name="decrease_cart"),
]
