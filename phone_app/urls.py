from django.contrib import admin
from django.urls import path
from phone_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cart/<int:id>',views.cart,name='cart'),
    path('cart',views.cart,name='cart'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('session',views.logout,name='session'),
    path('email',views.email,name='email'),
    path('forgot',views.forgot,name='forgot'),
    path('reset',views.reset,name='reset'),
    path('password',views.password,name='password'),
    path('delete',views.remove,name='remove'),
    path('clear',views.clear,name='clear'),
]