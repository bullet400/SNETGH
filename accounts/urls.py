from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns =[
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:cust_id>/', views.customers, name='customers'),
    path('creat_order/<str:pk>/', views.create_order, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('del_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('create_cust/', views.creat_customer, name="creat_customer"),
    path('update_cust/<str:cust_id>/', views.update_customer, name="update_customer"),
    path('del_cust/<int:cust_id>/', views.delete_customer, name="delete_customer"),
    path('delete_order/<int:order_id>/', views.del_order, name="delete_order"),
    path('pay/', views.payment, name='payment'),
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('users/', views.customerPage, name='user'),
    
    
]