from django.contrib import admin
from django.urls import path
from phone_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('home',views.home,name='home')
]