from django.urls import path
from . import views


urlpatterns = [
    path('category/', views.category, name='category'),
    path('category/<slug:slug>/', views.single_cat, name='single_cat'),
]