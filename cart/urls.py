from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('add_cart/<slug:slug>/', views.add_cart, name="add_cart"),
    path('remove_cart/<slug:slug>/', views.remove_cart, name="remove_cart"),
]
