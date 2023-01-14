from django.urls import path
from . import views


urlpatterns = [
    path('single_product/<slug:slug>/', views.single_product, name='single_product'),
]
